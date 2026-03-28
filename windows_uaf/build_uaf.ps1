# Compile your exploit lab
Write-Host "[+] Compiling Vulnerable UAF Binary..." -ForegroundColor Cyan
cl.exe /Zi /GS- /D"_CRT_SECURE_NO_WARNINGS" uaf.c /link /DYNAMICBASE:NO /NXCOMPAT:NO /OUT:uaf.exe

if ($LASTEXITCODE -eq 0) {
    Write-Host "[+] SUCCESS: uaf.exe is ready." -ForegroundColor Green
} else {
    Write-Host "[!] FAILED: Check the errors above." -ForegroundColor Red
}

