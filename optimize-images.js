const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const IMAGES_DIR = path.join(__dirname, 'src', 'images');
const MAX_WIDTH = 1600;
const JPEG_QUALITY = 80;
const PNG_QUALITY = 80;

async function optimizeImages() {
  const files = fs.readdirSync(IMAGES_DIR);
  let saved = 0;
  let totalBefore = 0;
  let totalAfter = 0;

  for (const file of files) {
    const ext = path.extname(file).toLowerCase();
    if (!['.jpg', '.jpeg', '.png', '.webp'].includes(ext)) continue;

    const filepath = path.join(IMAGES_DIR, file);
    const stat = fs.statSync(filepath);
    const sizeMB = stat.size / 1024 / 1024;

    // Skip small images
    if (sizeMB < 0.3) continue;

    totalBefore += stat.size;

    try {
      const img = sharp(filepath);
      const meta = await img.metadata();

      let pipeline = sharp(filepath);

      // Resize if wider than MAX_WIDTH
      if (meta.width && meta.width > MAX_WIDTH) {
        pipeline = pipeline.resize(MAX_WIDTH, null, { withoutEnlargement: true });
      }

      // Compress based on format
      if (ext === '.png') {
        pipeline = pipeline.png({ quality: PNG_QUALITY, compressionLevel: 9 });
      } else {
        pipeline = pipeline.jpeg({ quality: JPEG_QUALITY, mozjpeg: true });
      }

      const buffer = await pipeline.toBuffer();
      
      // Only write if actually smaller
      if (buffer.length < stat.size) {
        fs.writeFileSync(filepath, buffer);
        const newSize = buffer.length / 1024 / 1024;
        totalAfter += buffer.length;
        console.log(`  ${file}: ${sizeMB.toFixed(1)}MB → ${newSize.toFixed(1)}MB`);
        saved++;
      } else {
        totalAfter += stat.size;
      }
    } catch (err) {
      console.log(`  ! ${file}: ${err.message}`);
      totalAfter += stat.size;
    }
  }

  console.log(`\nOptimized ${saved} images`);
  console.log(`Total: ${(totalBefore/1024/1024).toFixed(1)}MB → ${(totalAfter/1024/1024).toFixed(1)}MB`);
}

optimizeImages().catch(console.error);
