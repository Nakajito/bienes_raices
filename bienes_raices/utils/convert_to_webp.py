"""
Script para convertir imágenes (JPG, JPEG, PNG) a formato WebP con compresión optimizada.
Procesa recursivamente todas las subcarpetas dentro de assets/media.
Genera versiones responsive (400, 800, 1200 px de ancho) y las guarda en assets/public/media-webp/
manteniendo la estructura de carpetas original.
"""

from PIL import Image
from pathlib import Path
import sys


# Configuración - ajustada para la estructura real del proyecto
PROJECT_ROOT = Path(__file__).parent.parent.parent  # sube 3 niveles desde utils/
SRC_DIR = PROJECT_ROOT / "assets" / "media"
DST_DIR = PROJECT_ROOT / "assets" / "public" / "media-webp"
SIZES = [400, 800, 1200]  # anchos responsive en píxeles
QUALITY = 80  # calidad WebP (0-100, recomendado 75-85)
METHOD = 6  # método de compresión WebP (0-6, 6 = más lento pero mejor)


def convert_images():
    """Convierte todas las imágenes JPG/PNG a WebP en varios tamaños recursivamente."""
    if not SRC_DIR.exists():
        print(f"❌ Error: carpeta fuente no existe: {SRC_DIR}")
        print(f"💡 Crea la carpeta o ajusta SRC_DIR en el script")
        sys.exit(1)

    DST_DIR.mkdir(parents=True, exist_ok=True)
    print(f"📂 Origen: {SRC_DIR}")
    print(f"📂 Destino: {DST_DIR}")
    print(f"🔧 Configuración: calidad={QUALITY}, tamaños={SIZES}\n")

    supported = [".jpg", ".jpeg", ".png"]
    # Buscar recursivamente en todas las subcarpetas
    images = [p for p in SRC_DIR.rglob("*.*") if p.suffix.lower() in supported]

    if not images:
        print(f"⚠️  No se encontraron imágenes en {SRC_DIR} ni subcarpetas")
        return

    print(f"🔍 Encontradas {len(images)} imágenes para procesar\n")

    total = 0
    for img_path in images:
        try:
            # Calcular ruta relativa para mantener estructura de carpetas
            relative_path = img_path.relative_to(SRC_DIR)
            relative_dir = relative_path.parent

            # Crear estructura de carpetas en destino
            output_dir = DST_DIR / relative_dir
            output_dir.mkdir(parents=True, exist_ok=True)

            with Image.open(img_path) as im:
                # convertir RGBA a RGB si es PNG con transparencia
                if im.mode in ("RGBA", "LA", "P"):
                    background = Image.new("RGB", im.size, (255, 255, 255))
                    if im.mode == "P":
                        im = im.convert("RGBA")
                    background.paste(
                        im, mask=im.split()[-1] if im.mode == "RGBA" else None
                    )
                    im = background

                for width in SIZES:
                    # calcular altura proporcional
                    ratio = width / im.width
                    height = int(im.height * ratio)

                    # redimensionar
                    im_resized = im.resize((width, height), Image.Resampling.LANCZOS)

                    # guardar WebP manteniendo estructura de carpetas
                    out_path = output_dir / f"{img_path.stem}-{width}.webp"
                    im_resized.save(
                        out_path,
                        "WEBP",
                        quality=QUALITY,
                        method=METHOD,
                    )

                    # info de archivo
                    original_size = img_path.stat().st_size / 1024  # KB
                    webp_size = out_path.stat().st_size / 1024  # KB
                    reduction = ((original_size - webp_size) / original_size) * 100

                    # mostrar ruta relativa para mejor legibilidad
                    rel_output = out_path.relative_to(DST_DIR)
                    print(
                        f"✅ {relative_path} → {rel_output} "
                        f"({original_size:.1f}KB → {webp_size:.1f}KB, -{reduction:.1f}%)"
                    )
                    total += 1

        except Exception as e:
            print(f"❌ Error procesando {img_path.name}: {e}")

    print(f"\n🎉 Completado: {total} imágenes WebP generadas en {DST_DIR}")
    print(f"📁 Estructura de carpetas preservada")


if __name__ == "__main__":
    convert_images()
