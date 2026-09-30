Add-Type -AssemblyName System.Drawing

$srcPath = Resolve-Path "Logo.png"
$src = [System.Drawing.Bitmap]::FromFile($srcPath)

# The colorful emblem is in rows 1 to 309, width 0 to 291
$cropRect = New-Object System.Drawing.Rectangle 0, 1, 292, 309
$emblem = New-Object System.Drawing.Bitmap 292, 309
$g = [System.Drawing.Graphics]::FromImage($emblem)
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
$g.DrawImage($src, (New-Object System.Drawing.Rectangle 0, 0, 292, 309), $cropRect, [System.Drawing.GraphicsUnit]::Pixel)
$g.Dispose()
$src.Dispose()

function Generate-Favicon($size, $outputPath) {
    $bmp = New-Object System.Drawing.Bitmap $size, $size
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
    $g.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
    $g.Clear([System.Drawing.Color]::Transparent)

    # Slight padding so it doesn't touch the extreme border
    $pad = [float]($size * 0.04)
    $drawSize = [float]($size - (2 * $pad))
    $g.DrawImage($emblem, $pad, $pad, $drawSize, $drawSize)
    $g.Dispose()

    $bmp.Save($outputPath, [System.Drawing.Imaging.ImageFormat]::Png)
    $bmp.Dispose()
    Write-Host "Generated: $outputPath ($($size)x$($size))"
}

# Generate in root
Generate-Favicon 32 "favicon-32x32.png"
Generate-Favicon 192 "favicon.png"
Generate-Favicon 16 "favicon-16x16.png"
Generate-Favicon 180 "apple-touch-icon.png"

# Copy to cytos-react/public and cytos-react/dist
$targets = @("cytos-react/public", "cytos-react/dist")
foreach ($t in $targets) {
    if (Test-Path $t) {
        Copy-Item "favicon-32x32.png" (Join-Path $t "favicon-32x32.png") -Force
        Copy-Item "favicon.png" (Join-Path $t "favicon.png") -Force
        Copy-Item "favicon-16x16.png" (Join-Path $t "favicon-16x16.png") -Force
        Copy-Item "apple-touch-icon.png" (Join-Path $t "apple-touch-icon.png") -Force
        Write-Host "Copied favicons to $t"
    }
}

$emblem.Dispose()
Write-Host "All favicons generated and synced!"
