SBFspot.exe -scan > address.txt
python write-address.py
SBFspot.exe -nosql -v5 -ad30 -am0 -ae0 -startdate:20010810
@echo off
setlocal enabledelayedexpansion

:: Loop through all folders in .\smadata\ that start with "2"
for /d %%D in (.\smadata\2*) do (
    echo Processing folder: %%D

    :: Copy scripts into the target folder
    copy /Y transform.py "%%D\"
    copy /Y plot.py "%%D\"

    :: Change into the folder
    pushd "%%D"

    :: Run transform.py
    echo Running transform.py in %%D
    python transform.py

    :: Run plot.py
    echo Running plot.py in %%D
    python plot.py

    :: Go back to original directory
    popd

    echo Done with %%D
    echo -------------------------
)

echo All folders processed.
pause