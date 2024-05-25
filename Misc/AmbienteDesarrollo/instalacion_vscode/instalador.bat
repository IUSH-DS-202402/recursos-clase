curl https://vscode.download.prss.microsoft.com/dbazure/download/stable/019f4d1419fbc8219a181fab7892ebccf7ee29a2/VSCodeUserSetup-x64-1.87.0.exe -o vscode-inst.exe
start /wait "" vscode-inst.exe /VERYSILENT /MERGETASKS=!runcode
del vscode-inst.exe