#include <windows.h>
#include <iostream>

int main() {
    std::cout << "Attempting to load DobotDll.dll..." << std::endl;
    HMODULE hMod = LoadLibraryA("DobotDll.dll");
    
    if (hMod == NULL) {
        DWORD err = GetLastError();
        std::cout << "Failed to load DLL! Windows Error Code: " << err << std::endl;
        if (err == 193) {
            std::cout << "Error 193 means %1 is not a valid Win32 application (32-bit / 64-bit mismatch)." << std::endl;
        }
    } else {
        std::cout << "DLL loaded successfully!" << std::endl;
        FreeLibrary(hMod);
    }
    return 0;
}
