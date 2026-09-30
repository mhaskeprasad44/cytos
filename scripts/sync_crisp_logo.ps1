Add-Type -AssemblyName System.Drawing

$root = (Resolve-Path ".").Path
$srcLogoPath = Join-Path $root "scripts\cropped_new_logo.png"
if (-not (Test-Path $srcLogoPath)) {
    Write-Error "scripts\cropped_new_logo.png not found!"
    exit 1
}

$bmp = [System.Drawing.Bitmap]::FromFile($srcLogoPath)

# Copy to public and dist with exact filename
$dirs = @((Join-Path $root "public"), (Join-Path $root "dist"))
foreach ($d in $dirs) {
    if (-not (Test-Path $d)) {
        New-Item -ItemType Directory -Path $d -Force | Out-Null
    }
    
    $bmp.Save((Join-Path $d "CyTOS New Logo.png"), [System.Drawing.Imaging.ImageFormat]::Png)
    $bmp.Save((Join-Path $d "CyTOS-New-Logo.png"), [System.Drawing.Imaging.ImageFormat]::Png)
    $bmp.Save((Join-Path $d "Logo.png"), [System.Drawing.Imaging.ImageFormat]::Png)
    $bmp.Save((Join-Path $d "Logo-cropped.png"), [System.Drawing.Imaging.ImageFormat]::Png)
    $bmp.Save((Join-Path $d "Logo-footer.png"), [System.Drawing.Imaging.ImageFormat]::Png)

    $imgDir = Join-Path $d "assets\images"
    if (Test-Path $imgDir) {
        $bmp.Save((Join-Path $imgDir "CyTOS New Logo.png"), [System.Drawing.Imaging.ImageFormat]::Png)
        $bmp.Save((Join-Path $imgDir "CyTOS-New-Logo.png"), [System.Drawing.Imaging.ImageFormat]::Png)
        $bmp.Save((Join-Path $imgDir "Logo.png"), [System.Drawing.Imaging.ImageFormat]::Png)
        $bmp.Save((Join-Path $imgDir "Logo-cropped.png"), [System.Drawing.Imaging.ImageFormat]::Png)
    }
    Write-Host "Updated all logo files in $d"
}

$bmp.Dispose()
Write-Host "All logo files now carry the crisp CyTOS New Logo!"
