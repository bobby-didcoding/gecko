DJANGO_APPS=(
  "backend-api"
  "frontend-spa"
  "ipfs-node"
  "main-site"
)

FRAMEWORK_ENVS=(
    "STRIPE_PUBLISHABLE"
    "STRIPE_SECRET"
  )

API_ENVS=(
    "OPERATOR_ID"
    "OPERATOR_KEY"
    "OPERATOR_PRIVATE_KEY"
    "IPFS_API_KEY"
    "DO_KEY"
    "NOWPAYMENTS_API_KEY"
    "FIXER_API_KEY"
    "COINLAYER_API_KEY"
    "COINBASE_API_KEY"
    "COINBASE_PROFILE_API_KEY"
    "COIN_MARKET_CAP_API_KEY"
    "STRIPE_PUBLISHABLE"
    "STRIPE_SECRET"
    "EMAIL_PASSWORD"
    "FIELD_ENCRYPTION_KEY"
)

SPA_ENVS=(
    "DISCORD_APP_ID"
    "DISCORD_APP_PUBLIC_KEY"
    "DISCORD_TOKEN"
    "DISCORD_ROLE_ONE"
    "DISCORD_ROLE_TWO"
    "DISCORD_ROLE_THREE"
    "DISCORD_ROLE_CHANNEL"
    "SENTX_API_KEY"
    "ODDERSEA_API_SECRET"
    "EMAIL_PASSWORD"
    "RECAPTCHA_PUBLIC_KEY"
    "RECAPTCHA_PRIVATE_KEY"
  )

MAIN_ENVS=(
    "OPERATOR_ID"
    "OPERATOR_KEY"
    "OPERATOR_PRIVATE_KEY"
    "ODDERSEA_API_SECRET"
    "RECAPTCHA_PUBLIC_KEY"
    "RECAPTCHA_PRIVATE_KEY"
    "GOOGLE_API_KEY"
    "GOOGLE_ALLOWED_COUNTRIES"
    "GOOGLE_ANALYTICS_PROPERTY_ID"
    "GOOGLE_TAG_ID"
    "EMAIL_PASSWORD"
  )

get_api_envs (){
    echo "Fetching API secrets from Google Cloud...\n"
    for secret in "${API_ENVS[@]}"
    do
        if [ ! -d $secret ]; then
            $value= make gcloud-get-secret $secret
            echo $value >> ./backend-api/.env
        fi
    done
}

get_spa_envs (){
    echo "Fetching SPA secrets from Google Cloud...\n"
    for secret in "${SPA_ENVS[@]}"
    do
        if [ ! -d $secret ]; then
            $value= make gcloud-get-secret $secret
            echo $value >> ./frontend-spa/.env
        fi
    done
}

get_main_envs (){
    echo "Fetching Main website secrets from Google Cloud...\n"
    for secret in "${MAIN_ENVS[@]}"
    do
        if [ ! -d $secret ]; then
            $value= make gcloud-get-secret $secret
            echo $value >> ./main-site/.env
        fi
    done
}

add_directory_cms_secrets_to_template (){
    vars=($(get_directory_cms_envs))
    for var in "${vars[@]}"
        do
            echo $var >> ./directory-cms/conf/env/secrets-do-not-commit
        done
}

get_ipfs_api_key (){
   make get-ipfs-api-key
}

get_api_key (){
   make get-api-key
}

add_ipfs_api_key_to_templates (){
    vars=($(get_ipfs_api_key))
    echo ${vars[6]} >> ./backed-api/.env
}

add_api_key_to_templates (){
    vars=($(get_api_key))
    echo ${vars[6]} >> ./frontend-spa/.env
    echo ${vars[6]} >> ./main-site/.env
}

echo "#######################################################\n\n \
Lets get started \n\n\
#######################################################\n\n"

echo "what is your GitHub username?: "
read username

echo "\n#######################################################\n\n \
Welcome ${username}! \n\n\
#######################################################\n\n"

echo "what is your GitHub personal access token?: "
read password

read -e -p "Would you like to clone repositories? [Y/n] " YN

if [[ $YN != "n" && $YN != "N" && $YN != "" ]]; then
    echo "Start initalising repositories...\n"
    for app in "${DJANGO_APPS[@]}"
    do
        echo "Initalising: $app"

        if [ ! -d $app ]; then
            git clone https://$username:$password@github.com/Oddersea/$app.git ./$app
        fi

    done
fi

echo "#######################################################\n\n \
Creating secrets... \n\n\
#######################################################\n\n"

if [ ! -f ./.env ]; \
    then cp secrets/framework .env \
        && echo "Created .env";
    else echo ".env already exists. Delete it first to recreate it."; \
fi
if [ ! -f ./backend-api/.env ]; \
    then cp secrets/backend-api backend-api/.env \
        && echo "Created ./backend-api/.env";
        get_api_envs
    else echo "backend-api/.env already exists. Delete it first to recreate it."; \
fi
if [ ! -f ./frontend-spa/.env ]; \
    then cp secrets/frontend-spa frontend-spa/.env \
        && echo "Created ./frontend-spa/.env";
        get_spa_envs
    else echo "frontend-spa/.env already exists. Delete it first to recreate it."; \
fi
if [ ! -f ./main-site/.env ]; \
    then cp secrets/main-site main-site/.env \
        && echo "Created ./main-site/.env";
        get_main_envs
    else echo "main-site/.env already exists. Delete it first to recreate it."; \
fi
if [ ! -f ./ipfs-node/.env ]; \
    then cp secrets/ipfs-node ipfs-node/.env \
        && echo "Created ./ipfs-node/.env"; \
    else echo "ipfs-node/.env already exists. Delete it first to recreate it."; \
fi


echo "#######################################################\n\n \
Initilizing ipfs-node... \n\n\
#######################################################\n\n"
make build-container ipfs-node

echo "ipfs-node must fully initialize before he next step \
Please look in the ipfs-node docker desktop logs for the following: \
\
System check identified 2 issues (0 silenced). \
2023-06-20 16:24:38 June 20, 2023 - 15:24:38 \
2023-06-20 16:24:38 Django version 4.1.9, using settings 'conf.settings' \
2023-06-20 16:24:38 Starting development server at http://0.0.0.0:8070/ \
2023-06-20 16:24:38 Quit the server with CONTROL-C. \
\
"

read -e -p "Check Docker Desktop, has ipfs-node finished initilizing? [Y/n] " YN

if [[ $YN != "y" && $YN != "Y" && $YN != "" ]]; then
    exit 1
fi

echo "#######################################################\n\n \
Getting ipfs-node api key for backend-api... \n\n\
#######################################################\n\n"

add_ipfs_api_key_to_templates

echo "#######################################################\n\n \
Initilizing backend-api... \n\n\
#######################################################\n\n"
make build-container backend-api

echo "backend-api must fully initialize before he next step \
Please look in the backend-api docker desktop logs for the following: \
\
System check identified 2 issues (0 silenced). \
2023-06-20 16:24:38 June 20, 2023 - 15:24:38 \
2023-06-20 16:24:38 Django version 4.1.9, using settings 'conf.settings' \
2023-06-20 16:24:38 Starting development server at http://0.0.0.0:8070/ \
2023-06-20 16:24:38 Quit the server with CONTROL-C. \
\
"

read -e -p "Check Docker Desktop, has backend-api finished initilizing? [Y/n] " YN

if [[ $YN != "y" && $YN != "Y" && $YN != "" ]]; then
    exit 1
fi

echo "#######################################################\n\n \
Getting backend-api api key for frontend-spa and main-site... \n\n\
#######################################################\n\n"

add_api_key_to_templates

echo "#######################################################\n\n \
Initilizing... \n\n\
#######################################################\n\n"
make build

echo "The entire project must be fully operational before we prime our databases \
Please look at docker descktop. We are looking for: \
\
1) Green ticks against all containers \
2) Completed migrations \
3) All servers running \
\
"

read -e -p "Are all 3 points listed above complete on all containers? [Y/n] " YN

if [[ $YN != "y" && $YN != "Y" && $YN != "" ]]; then
    exit 1
fi

make prime-spa-config
make prime-api-config
make prime-api-art
make prime-api-land
make prime-api-odd
make prime-api-token


echo "#######################################################\n\n \
*** Congratulations *** \n\n\
Everything should now be up and running \n\n\
#######################################################\n\n"
exit 1