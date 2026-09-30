Add-Type -AssemblyName System.Drawing

$root = (Resolve-Path ".").Path
$srcLogoPath = Join-Path $root "dist\CyTOS New Logo.png"
if (-not (Test-Path $srcLogoPath)) {
    $srcLogoPath = "C:\Users\PrasadMhaske\Downloads\CyTOS New Logo.png"
}

Write-Host "Loading source logo from: $srcLogoPath"
$srcBmp = [System.Drawing.Bitmap]::FromFile($srcLogoPath)

# 1. Calculate non-transparent bounds
$minX = $srcBmp.Width; $minY = $srcBmp.Height; $maxX = 0; $maxY = 0
for ($y = 0; $y -lt $srcBmp.Height; $y++) {
    for ($x = 0; $x -lt $srcBmp.Width; $x++) {
        $c = $srcBmp.GetPixel($x, $y)
        if ($c.A -gt 15) {
            if ($x -lt $minX) { $minX = $x }
            if ($x -gt $maxX) { $maxX = $x }
            if ($y -lt $minY) { $minY = $y }
            if ($y -gt $maxY) { $maxY = $y }
        }
    }
}

$cWidth = $maxX - $minX + 1
$cHeight = $maxY - $minY + 1
Write-Host "Content bounds: X=$minX..$maxX, Y=$minY..$maxY (Size: ${cWidth}x${cHeight})"

# 2. Crop full logo (Emblem + CyTOS + Tagline) tightly
$cropRect = New-Object System.Drawing.Rectangle $minX, $minY, $cWidth, $cHeight
$fullLogo = New-Object System.Drawing.Bitmap $cWidth, $cHeight
$gFull = [System.Drawing.Graphics]::FromImage($fullLogo)
$gFull.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$gFull.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$gFull.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
$gFull.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
$gFull.Clear([System.Drawing.Color]::Transparent)
$gFull.DrawImage($srcBmp, (New-Object System.Drawing.Rectangle 0, 0, $cWidth, $cHeight), $cropRect, [System.Drawing.GraphicsUnit]::Pixel)
$gFull.Dispose()

# 3. Crop Emblem Only for Favicon (from top to row 216 of the cropped logo)
# Emblem height is 216 relative to cropped logo
$emblemHeight = 216
$emblemCropRect = New-Object System.Drawing.Rectangle $minX, $minY, $cWidth, $emblemHeight
$emblem = New-Object System.Drawing.Bitmap $cWidth, $emblemHeight
$gEmb = [System.Drawing.Graphics]::FromImage($emblem)
$gEmb.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$gEmb.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$gEmb.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
$gEmb.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
$gEmb.Clear([System.Drawing.Color]::Transparent)
$gEmb.DrawImage($srcBmp, (New-Object System.Drawing.Rectangle 0, 0, $cWidth, $emblemHeight), $emblemCropRect, [System.Drawing.GraphicsUnit]::Pixel)
$gEmb.Dispose()

# 4. Helper function to generate square favicons with subtle padding
function Save-Favicon($sourceImg, $size, $destPath) {
    $bmp = New-Object System.Drawing.Bitmap $size, $size
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
    $g.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
    $g.Clear([System.Drawing.Color]::Transparent)

    # Maintain aspect ratio within square
    $srcW = $sourceImg.Width
    $srcH = $sourceImg.Height
    $scale = [Math]::Min([float]$size / $srcW, [float]$size / $srcH) * 0.94 # 3% padding around
    $drawW = [float]($srcW * $scale)
    $drawH = [float]($srcH * $scale)
    $drawX = [float](($size - $drawW) / 2.0)
    $drawY = [float](($size - $drawH) / 2.0)

    $g.DrawImage($sourceImg, $drawX, $drawY, $drawW, $drawH)
    $g.Dispose()

    $bmp.Save($destPath, [System.Drawing.Imaging.ImageFormat]::Png)
    $bmp.Dispose()
    Write-Host "Created Favicon ($size x $size): $destPath"
}

# 5. Output targets
$targetDirs = @(
    (Join-Path $root "public"),
    (Join-Path $root "dist")
)

foreach ($dir in $targetDirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }

    # Save original user file
    Copy-Item $srcLogoPath (Join-Path $dir "CyTOS New Logo.png") -Force
    Copy-Item $srcLogoPath (Join-Path $dir "CyTOS-New-Logo.png") -Force

    # Save cropped full logo as Logo.png, Logo-cropped.png, Logo-footer.png
    $fullLogo.Save((Join-Path $dir "Logo.png"), [System.Drawing.Imaging.ImageFormat]::Png)
    $fullLogo.Save((Join-Path $dir "Logo-cropped.png"), [System.Drawing.Imaging.ImageFormat]::Png)
    $fullLogo.Save((Join-Path $dir "Logo-footer.png"), [System.Drawing.Imaging.ImageFormat]::Png)

    # In assets/images
    $imgSubdir = Join-Path $dir "assets\images"
    if (Test-Path $imgSubdir) {
        Copy-Item $srcLogoPath (Join-Path $imgSubdir "CyTOS New Logo.png") -Force
        Copy-Item $srcLogoPath (Join-Path $imgSubdir "CyTOS-New-Logo.png") -Force
        $fullLogo.Save((Join-Path $imgSubdir "Logo.png"), [System.Drawing.Imaging.ImageFormat]::Png)
        $fullLogo.Save((Join-Path $imgSubdir "Logo-cropped.png"), [System.Drawing.Imaging.ImageFormat]::Png)
    }

    # Generate favicons
    Save-Favicon $emblem 16 (Join-Path $dir "favicon-16x16.png")
    Save-Favicon $emblem 32 (Join-Path $dir "favicon-32x32.png")
    Save-Favicon $emblem 180 (Join-Path $dir "apple-touch-icon.png")
    Save-Favicon $emblem 192 (Join-Path $dir "favicon.png")
}

$srcBmp.Dispose()
$fullLogo.Dispose()
$emblem.Dispose()
Write-Host "Logo and favicon generation completed successfully!"
