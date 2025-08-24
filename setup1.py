import platform
b = platform.architecture()[0]
if b == '64bit':
    import termux_setup
    termux_setup.banner_menu()
else:
     print("033[1;32m\033[1m32bit\033[0m\033[1;31m\033[1m Not Supported!")
