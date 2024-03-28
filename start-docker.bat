SETLOCAL ENABLEDELAYEDEXPANSION
@echo off 

SET DJANGO_APPS=api app ipfs-api main-website framework

copy envs\framework .env

FOR %%a in (%DJANGO_APPS%) do (
  if %%a==framework (
    FOR /f %%c in (secrets-new\%%a) do (
      ECHO Attempting to get %%c from Google Cloud
      FOR /F %%d in ('gcloud secrets versions access latest --secret=%%c') DO (
        ECHO %%c=%%d >> .env
      )
    )
  ) ELSE (
    ECHO Cloning %%a
    call git clone --branch develop https://github.com/Oddersea/%%a.git ./%%a
    copy envs-new\%%a %%a\app\backend\.env
    if %%a==api (
      robocopy api\app\backend\media api\app\backend\mediafiles /E
    )
    if %%a==app (
      robocopy app\app\backend\media app\app\backend\mediafiles /E
    )
    FOR /f %%c in (secrets-new\%%a) do (
      ECHO Attempting to get %%c from Google Cloud
      FOR /F %%d in ('gcloud secrets versions access latest --secret=%%c') DO (
        ECHO %%c=%%d >> ./%%a/app/backend/.env
      )
    )
  )
)

ECHO Attempting to get secrets from Google Cloud
    FOR /F %%d in ('gcloud secrets versions access latest --secret=%%c') DO (
      if %%a==framework (ECHO %%c=%%d >> ./.env) else (ECHO %%c=%%d >> ./%%a/app/backend/.env)
    )

ECHO Staring IPFS

call make build-container-new ipfs-api

ECHO Finished IPFS

set /p hasIpfsFinished= Has IPFS finished initilizing? y/n:

call make make-migrations-new ipfs-api
call make migrate-new ipfs-api


if %hasIpfsFinished%==y (
  ECHO Getting new IPFS api key
  FOR /F %%d in ('make get-ipfs-api-key-new') DO (
    IF not %%d==docker-compose if not %%d==my-remote-service ECHO IPFS_API_KEY=%%d >> ./api/app/backend/.env
  )
)

ECHO Staring Backend API

call make build-container-new api

ECHO Finished Backend API

set /p hasBackendApiFinished= Has Backend API finished initilizing? y/n:

if %hasBackendApiFinished%==y (
  call make make-migrations-new api
  call make migrate-new api
  ECHO Getting new API key
  FOR /F %%d in ('make get-api-key-new') DO (
    IF not %%d==docker-compose if not %%d==my-remote-service (
      ECHO ODDERSEA_API_SECRET=%%d >> ./app/app/backend/.env
      ECHO ODDERSEA_API_SECRET=%%d >> ./main-website/app/backend/.env
    )
  )
)

ECHO Staring Frontend App

call make build-container-new app

ECHO Finished Frontend App

set /p hasFrontendSpaFinished= Has Frontend App finished initilizing? y/n:

if %hasFrontendSpaFinished%==y (
  ECHO priming databases
  call make make-migrations-new app
  call make migrate-new app
  call make prime-spa-config-new
  call make prime-api-config-new
  call make prime-api-create-lottery-numbers-new
  call make prime-api-art-new
  call make prime-api-land-new
  call make prime-api-odd-new
  call make prime-api-token-new
  call make prime-api-new-art-new
  call make prime-api-deactivate-old-art-new
)

call make build-new

set /p hasbuildFinished= Has the build finished? y/n:

if %hasbuildFinished%==y (
  ECHO getting currencies
  call make get-currencies-new
)

ECHO Finished!! You should be all good to go.