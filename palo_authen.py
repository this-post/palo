__author__ = 'keerati'

import httplib, urllib, getpass, os, sys

#http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def check():
    print color.OKGREEN + '[+] Please wait while checking internet connection'
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        check_inter = httplib.HTTPConnection('google.com')
        check_inter.request('GET', '/', '', headers)
        response = check_inter.getresponse()
        res = response.reason
        if res == 'Found':
            print color.OKGREEN + '[+] It seem you have already login'
            exit()
        elif res == 'Moved Temporarily':
            while 1:
                is_attempt = raw_input(color.OKGREEN + '[+] You not login yet, Are you attempt to login now?(Y/N): ')
                if is_attempt == 'Y' or is_attempt == 'y':
                    attempt = 1
                    while 1:
                        user_val()
                        login(user_input, pass_input)
                        if login_res == 200:
                            if attempt == 3:
                                print color.FAIL + '[-] You are trying exceed limit'
                                exit()
                            print color.FAIL + '[-] Fail, Please try again(attempt=' + str(attempt) + ')'
                            attempt += 1
                        elif login_res == 302:
                            print color.OKGREEN + '[+] Success, Happy surfing'
                            break
                    break
                elif is_attempt == 'N' or is_attempt == 'n':
                    print color.OKGREEN + '[+] User exit'
                    exit()
    except:
        print color.FAIL + '[-] Unable to check'


def user_val():
    global user_input, pass_input
    user_input = raw_input(color.OKGREEN + '[+] Username: ')
    pass_input = getpass.getpass(color.OKGREEN + '[+] Password: ')
    return user_input, pass_input


def login(user,passwd):
    params = urllib.urlencode({'inputStr': '', 'escapeUser': user, 'user': user, 'passwd': passwd, 'ok': 'Login'})
    headers = {'User-Agent': 'Post Very Handsome', 'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    check_login = httplib.HTTPSConnection(sys.argv[1] + ':6082')
    check_login.request('POST', '/php/uid.php?vsys=1', params, headers)
    response = check_login.getresponse()
    global login_res
    login_res = response.status
    return login_res


if __name__ == '__main__':
    os.system('clear')
    print ' '
    print '          ____________     ___________     ________     ____________'
    print '         /  ______   /\   / _______  /\   /       /\   /           /\\'
    print '        /  /\    /  /  \ / /\     / /  \ / ______/  \ /____   ____/  \\'
    print '       /  /  \__/  /   // /  \___/ /   // /\     \  / \   /  /\   \  /'
    print '      /  /___/_/  /   // /   /  / /   // /__\_____\/   \_/  /  \___\/'
    print '     /  _________/   // /   /  / /   //        /\       /  /   /'
    print '    /  /\        \  // /   /  / /   //______  /  \     /  /   /'
    print '   /  /  \________\// /   /  / /   /  \    / /   /    /  /   /'
    print '  /  /   /         / /   /  / /   /____\__/ /   /    /  /   /'
    print ' /  /   /         / /___/__/ /   //        /   /    /  /   /'
    print '/__/   /         /__________/   //________/   /    /__/   /'
    print '\  \  /          \          \  / \        \  /     \  \  /'
    print ' \__\/            \__________\/   \________\/       \__\/'
    print ' '
    print color.HEADER + 'Palo Alto Captive Portal Authenticator\r\n'
    if len(sys.argv) != 2:
        print color.WARNING + '[!] Usage: ' + sys.argv[0] + ' ' + '[GW(Palo) IP]'
        exit()
    check()
