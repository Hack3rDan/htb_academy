



typedef struct _STARTUPINFOA{
    DWORD cb;
    LPSTR reserved;
    LPSTR lpDesktop;
    LPSTR lpTitle;
    DWORD dwX;
    DWORD dwY;
    DWORD dwXSize;
    DWORD dwYSize;
    DWORD dwXCountChars;
    DWORD dwYCountChars;
    DWORD dwFillAtribute;
    DWORD dwFlags;
    WORD wShowWindow;
    WORD cbReserved2;
    PBYTE lpReserved2;
    HANDLE hStdInput;
    HANDLE hStdOutput;
    HANDLE hStdError;
};

// Find addresses of needed functionsj

// Create a Socket and connect

// execute cmd.exe with reidrection
CreateProcessA(
    LPCSTR lpApplicationName,
    LPCSTR lpCommandLine,
    lpProcessAttributes,
    lpThreadAttributes,
    bInheritHandles,
    dwCreationFlags,
    lpEnvironment,
    lpCurrentDirectory.
    lpStartupInfo,
    lpProcessInformation)

