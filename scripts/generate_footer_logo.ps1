Add-Type -AssemblyName System.Drawing

$srcPath = (Resolve-Path "public/CyTOS New Logo.png").Path
$bmp = New-Object System.Drawing.Bitmap($srcPath)

# Create a new 32-bit ARGB bitmap
$outBmp = New-Object System.Drawing.Bitmap($bmp.Width, $bmp.Height, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)

$convertedCount = 0
for ($y = 0; $y -lt $bmp.Height; $y++) {
    for ($x = 0; $x -lt $bmp.Width; $x++) {
        $c = $bmp.GetPixel($x, $y)
        
        # In the bottom area (Y >= 210) where text is located
        if ($y -ge 210 -and $c.A -gt 15) {
            # Check if this pixel is part of the dark text ('C', 'y', tagline)
            # Gold pixels have high Red and Green relative to Blue, e.g. R > 120, G > 70, R > B + 30
            $isGold = ($c.R -gt 110 -and $c.G -gt 60 -and ($c.R -gt $c.B + 25))
            
            if (-not $isGold) {
                # This is dark text!
                # Calculate how dark it is:
                $lum = [int]($c.R * 0.299 + $c.G * 0.587 + $c.B * 0.114)
                if ($lum -lt 140) {
                    # Convert to pure white, maintaining full alpha
                    $newPixel = [System.Drawing.Color]::FromArgb($c.A, 255, 255, 255)
                    $outBmp.SetPixel($x, $y, $newPixel)
                    $convertedCount++
                    continue
                }
            }
        }
        
        # Otherwise copy original pixel
        $outBmp.SetPixel($x, $y, $c)
    }
}

Write-Host "Converted $convertedCount dark text pixels to pure white."

$whitePath = (Join-Path (Get-Location) "public/CyTOS-New-Logo-White.png")
$footerPath = (Join-Path (Get-Location) "public/Logo-footer.png")
$assetsWhitePath = (Join-Path (Get-Location) "public/assets/images/CyTOS-New-Logo-White.png")
$assetsFooterPath = (Join-Path (Get-Location) "public/assets/images/Logo-footer.png")

$outBmp.Save($whitePath, [System.Drawing.Imaging.ImageFormat]::Png)
$outBmp.Save($footerPath, [System.Drawing.Imaging.ImageFormat]::Png)
$outBmp.Save($assetsWhitePath, [System.Drawing.Imaging.ImageFormat]::Png)
$outBmp.Save($assetsFooterPath, [System.Drawing.Imaging.ImageFormat]::Png)

Write-Host "Saved white-text logo variants successfully!"

$bmp.Dispose()
$outBmp.Dispose()
