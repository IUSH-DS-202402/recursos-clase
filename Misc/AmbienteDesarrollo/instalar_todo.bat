cd instalacion_miniconda
call instalador.bat
cd ..\instalacion_vscode\
call instalador.bat
cd ..\instalar_bibliotecas_python
:: cd instalar_bibliotecas_python
call %UserProfile%\Miniconda3\Scripts\activate.bat %UserProfile%\Miniconda3
call instalar_bibliotecas_conda.bat
call instalar_bibliotecas_pip.bat
pause