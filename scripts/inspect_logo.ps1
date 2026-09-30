Add-Type -AssemblyName System.Drawing
$b = [System.Drawing.Bitmap]::FromFile((Resolve-Path "scripts/cropped_new_logo.png").Path)
Write-Host "Width: $($b.Width), Height: $($b.Height)"

for ($y = 190; $y -le 240; $y += 2) {
    $nonTrans = 0
    for ($x = 0; $x -lt $b.Width; $x++) {
        if ($b.GetPixel($x, $y).A -gt 20) { $nonTrans++ }
    }
    Write-Host ("Row {0}: {1} non-trans pixels" -f $y, $nonTrans)
}
$b.Dispose()
