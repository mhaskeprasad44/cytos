Add-Type -AssemblyName System.Drawing
$bmp = New-Object System.Drawing.Bitmap((Resolve-Path "public/Logo-footer.png").Path)

Write-Host "ASCII Map of Footer Logo Y=215..310 (Step Y=3, Step X=3):"
Write-Host "W = White pixel (#ffffff), . = Gold pixel, ' ' = transparent"
for ($y = 215; $y -lt $bmp.Height; $y += 3) {
    $line = ""
    for ($x = 0; $x -lt $bmp.Width; $x += 3) {
        $c = $bmp.GetPixel($x, $y)
        if ($c.A -lt 40) {
            $line += " "
        } else {
            if ($c.R -gt 240 -and $c.G -gt 240 -and $c.B -gt 240) {
                # White pixel!
                $line += "W"
            } elseif ($c.R -gt 120 -and $c.G -gt 70) {
                # Gold pixel
                $line += "."
            } else {
                $line += ":"
            }
        }
    }
    if ($line.Trim().Length -gt 0) {
        Write-Host $line
    }
}

$bmp.Dispose()
