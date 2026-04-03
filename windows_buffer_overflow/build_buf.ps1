param(
    [string]$file_name = "file.c"
    
)

# Setup Vars
$exe_name = $file_name.Replace(".c",".exe")


# Compile your exploit lab
Write-Host "[+] Compiling Vulnerable UAF Binary..." -ForegroundColor Cyan
cl.exe /Zi /GS /D"_CRT_SECURE_NO_WARNINGS" $file_name /link /DYNAMICBASE:NO /NXCOMPAT:NO /OUT:$exe_name

if ($LASTEXITCODE -eq 0) {
    Write-Host "[+] SUCCESS: $exe_name is ready." -ForegroundColor Green
} else {
    Write-Host "[!] FAILED: Check the errors above." -ForegroundColor Red
}

