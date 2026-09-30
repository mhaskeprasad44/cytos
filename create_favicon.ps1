Add-Type -AssemblyName System.Drawing
$logoPath = Resolve-Path "Logo-cropped.png"
$src = [System.Drawing.Image]::FromFile($logoPath)
Write-Host "Original logo dimensions: $($src.Width) x $($src.Height)"

$maxDim = [Math]::Max($src.Width, $src.Height)
$square = New-Object System.Drawing.Bitmap $maxDim, $maxDim
$g = [System.Drawing.Graphics]::FromImage($square)
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
$g.Clear([System.Drawing.Color]::Transparent)

$x = ($maxDim - $src.Width) / 2
$y = ($maxDim - $src.Height) / 2
$g.DrawImage($src, [float]$x, [float]$y, [float]$src.Width, [float]$src.Height)
$g.Dispose()

# Create 64x64 favicon.png
$fav64 = New-Object System.Drawing.Bitmap 64, 64
$g2 = [System.Drawing.Graphics]::FromImage($fav64)
$g2.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g2.DrawImage($square, 0, 0, 64, 64)
$fav64.Save((Join-Path (Get-Location) "favicon.png"), [System.Drawing.Imaging.ImageFormat]::Png)
$g2.Dispose()

# Create 32x32 favicon-32x32.png
$fav32 = New-Object System.Drawing.Bitmap 32, 32
$g3 = [System.Drawing.Graphics]::FromImage($fav32)
$g3.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g3.DrawImage($square, 0, 0, 32, 32)
$fav32.Save((Join-Path (Get-Location) "favicon-32x32.png"), [System.Drawing.Imaging.ImageFormat]::Png)
$g3.Dispose()

$square.Dispose()
$src.Dispose()
Write-Host "Favicons generated successfully!"
