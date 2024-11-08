# Setup

## Dependencies

SkyPortal requires the following software to be installed.  We show
how to install them on MacOS and Debian-based systems below.

- Python 3.10 or later (<3.13, since `numba` requires <3.13)
- Supervisor (v>=4.2.1)
- NGINX (v>=1.7)
- PostgreSQL (v>=14.0)
- Node.JS/npm (v>=16.14.0/8.3.2)

When installing SkyPortal on Debian-based systems, 2 additional packages are required to be able to install `pycurl` later on:

- libcurl4-gnutls-dev
- libgnutls28-dev

## Source download, Python environment

Clone the [SkyPortal repository](https://github.com/skyportal/skyportal) and start a new
virtual environment.

```
git clone https://github.com/skyportal/skyportal.git
cd skyportal/
```
Create and activate a virtual environment with Python 3.10. We recommend using conda as it will handle Python version management for you:
```
conda create -n skyportal_env python=3.10
conda activate skyportal_env
```
Alternatively, if you prefer to usevirtualenv, first ensure you have Python 3.10 installed:
```
# Check your Python version
python3 --version

# If you need Python 3.10:
# On MacOS with Homebrew:
brew install python@3.10

# On Debian/Ubuntu:
sudo apt install python3.10
```

Then, create your virtual environment:
```
# Using virtualenv
virtualenv -p python3.10 skyportal_env
source skyportal_env/bin/activate
```
Note: If you need to upgrade your Python version in the future, it's recommended to create a new virtual environment rather than upgrading an existing one. You can create a new environment with a different name or remove the old one first with rm -rf skyportal_env (virtualenv) or conda env remove -n skyportal_env (conda).

You can also use `conda` or `pipenv` to create your environment.

If you developing on a Mac with an ARM (M1/M2) you might consider using a Rosetta-driven environment so that you more easily install dependencies (that tend to be x86-centric):

```
CONDA_SUBDIR=osx-64 conda create -n skyportal_env \
      python=3.10
conda activate skyportal_env
conda config --env --set subdir osx-64
conda config --add channels conda-forge
conda config --set channel_priority strict
```



If you are using Windows Subsystem for Linux (WSL) be sure you clone the repository onto a location on the virtual machine, not the mounted Windows drive. Additionally, we recommend that you use WSL 2, and not WSL 1, in order to avoid complications in interfacing with the Linux image's `localhost` network.

## Installation: MacOS

These instructions assume that you have [Homebrew](http://brew.sh/) installed.

1. Install project dependencies

Using Homebrew, install core dependencies:
```
brew install supervisor nginx postgresql node llvm libomp gsl rust
```
If you want to use [brotli compression](https://en.wikipedia.org/wiki/Brotli) with NGINX (better compression rates for the frontend), you can install NGINX with the `ngx_brotli` module with this command:
```
brew tap denji/nginx && brew install nginx-full --with-brotli
```

 _If you already had NGINX installed, you may need to uninstall it first with `brew unlink nginx`._ Otherwise, you can install NGINX normally with `brew install nginx`.

Then, install Node.js with NVM:
```
nvm install node
```
Finally, install these compression libraries. These are needed in order to install the Python dependency `tables` later on:
```
brew install hdf5 c-blosc lzo bzip2
```
After installing each package, Homebrew will print out the installation paths. You should add these paths to your `.zshrc` file to ensure SkyPortal can locate these libraries. Instructions for this can be found in the [Configuring Shell Environment for Development](#configure-shell-mac) section below.


2. Start the PostgreSQL server:

  - To start automatically at login: `brew services start postgresql`
  - To start manually: `pg_ctl -D /usr/local/var/postgres start`

  You may also need to run the following command to create the proper admin user.
  First, find your PostgreSQL installation path:
  ```
   # Try the opt directory first
   ls /opt/homebrew/opt/postgresql*/bin/createuser

   # If that doesn't work, try the Cellar directory
   ls /opt/homebrew/Cellar/postgresql*/*/bin/createuser
  ```
  One of these commands should show you the path to createuser. Use that path to create the admin user:

  ```bash
  /usr/local/opt/postgres/bin/createuser -s postgres
  ```

3. To run the test suite, you'll need Geckodriver:

	```
	brew install geckodriver
	```

4. To build the docs, you'll need graphviz:

	```
	brew install graphviz
	```

5. Activate the environment and add a few (hard-to install-with-pip) packages by hand:

	```
	conda activate skyportal_env
	conda install pyproj numba Shapely
	```

5. (ARM M1/M2) Explicitly [install ligo.skymap using conda rather than pip](https://lscsoft.docs.ligo.org/ligo.skymap/quickstart/install.html#option-2-conda):

   ```
   conda activate skyportal_env
   conda install ligo.skymap
   ```
<a name="configure-shell-mac"></a>
### Configuring Shell Environment for Development

When developing with SkyPortal on mac, you may  also need to configure your shell enviroment. Here is how you can do that by editing your `.zshrc` file.

#### Open your `.zshrc` file in a text editor:

```
nano ~/.zshrc
```
#### Set enviroment variables to their installation paths
After installing the libraries with Homebrew, you'll need to set environment variables to their installation paths. Replace the placeholder text `<path-to-library>` with the actual path that Homebrew provides upon sucessful installation.

```
export HDF5_DIR="<path-to-hdf5>"
export BLOSC_DIR="<path-to-c-blosc>"
export LZO_DIR="<path-to-lzo>"
export BZIP_DIR="<path-to-bzip2>"
```

Typically, Homebrew provides these paths upon successful installation. You can also discover where a library was installed by Homebrew with this command:

```
brew info <name_of_package>
```
#### Alias pip3 and python3
Depending on your system setup, the `python` and `pip` commands might point to Python 2 rather than Python 3. To ensure that you're using Python 3 and its corresponding pip version, you may need to set aliases in your `.zshrc` file:

```
alias pip='pip3'
alias python='python3'
```

#### To activate the changes, source your .zshrc file:
```
source ~/.zshrc
```
### Checking for Port Availability
SkyPortal defaults to using port 5000. However, this port may already be in use by MacPorts or other services. To verify if port 5000 is available, use the `lsof` command in the terminal.

```
lsof -i :5000
```
If the command outputs information about a service, it means that port 5000 is already in use. In this case, you may need to configure SkyPortal to use a different port.

## Installation: Debian-based Linux and WSL

1. Install dependencies

	```
	sudo apt install supervisor postgresql \
	      libpq-dev npm python3-pip \
	      libcurl4-gnutls-dev libgnutls28-dev
	```

	If you want to use [brotli compression](https://en.wikipedia.org/wiki/Brotli) with NGINX (better compression rates for the frontend), you have to install NGINX and the brotli module from another source with:

	```
	sudo apt remove -y nginx nginx-common nginx-core
	sudo add-apt-repository ppa:ondrej/nginx-mainline -y
	sudo apt update -y
	sudo apt install -y nginx libnginx-mod-brotli
	```

	Otherwise, you can install NGINX normally with `sudo apt-get install nginx`.

2. Configure your database permissions.

	In `pg_hba.conf` (typically located in
	`/etc/postgresql/<postgres-version>/main`), insert the following lines
	*before* any other `host` lines:

	```
	host skyportal skyportal 127.0.0.1/32 trust
	host skyportal_test skyportal 127.0.0.1/32 trust
	host all postgres 127.0.0.1/32 trust
	```

	If you are deploying SkyPortal using IPv6 rather than IPv4, you should add the following lines instead:

	```
	host skyportal skyportal ::1/128 trust
	host skyportal_test skyportal ::1/128 trust
	host all postgres ::1/128 trust
	```

	In some PostgreSQL installations, the default TCP port may be different from the 5432 value assumed in our default configuration file values. To remedy this, you can either edit your config.yaml file to reflect your system's PostgreSQL default port, or update your system-wide config to use port 5432 by editing /etc/postgresql/14/main/postgresql.conf (replace "14" with your installed version number) and changing the line `port = XXXX` (where "XXXX" is whatever the system default was) to `port = 5432`.

	Restart PostgreSQL:

	```
	sudo service postgresql restart
	```

3. To run the test suite, you'll need Geckodriver:

	- Download the latest version from https://github.com/mozilla/geckodriver/releases/
	- Extract the binary to somewhere on your path
	- Ensure it runs with `geckodriver --version`

	In later versions of Ubuntu (16.04+), you can install Geckodriver through apt:
	```
	sudo apt install firefox-geckodriver
	```

4. To build the docs, you'll need graphviz:

	```
	sudo apt install graphviz-dev graphviz
	```

## Launch

0. Make sure you are in the skyportal env: `conda activate skyportal_env`
1. Initialize the database with `make db_init` (this only needs to
   happen once).
2. Copy `config.yaml.defaults` to `config.yaml`.
3. Run `make log` to monitor the service and, in a separate window, `make run` to start the server.
4. Direct your browser to `http://localhost:5000`.
5. If you want some test data to play with, run `make load_demo_data` (do this while the server is running!).
6. Change users by navigating to `http://localhost:5000/become_user/<#>` where # is a number from 1-5.
   Different users have different privileges and can see more or less of the demo data.

## Troubleshooting

If you have trouble getting the demo data try doing

```make db_clear && make db_init && make run```

and then, from a different window, do `make load_demo_data`.

If you are using WSL, be sure everything (the git repository and all dependencies) are on the Linux machine and not the Windows side, as connection oddities can otherwise cause several errors.

Mac users may need to disable Airplay Receiver in System Preferences to free up port 5000 and avoid a 403 Forbidden error.

## Additional Configuration

The configuration file lives in `config.yaml`, and is meant to be
self-documenting.  Please modify as you see fit.

**Before deploying this on a public server** change `app:secret-key`
to a unique value.

If you want to use a different configuration file, you may launch any
of the SkyPortal commands with the FLAGS environment variable set:

```
FLAGS="--config=myconfig.yaml" make run
```

### Authentication

By default, the server allows anyone to log in (even if it presents a
login screen).  If you are running a public-facing instance of
SkyPortal, you should enable multi-user login by adding Google
credentials to the `server:auth` section of the configuration file and
setting `debug_login` to `False`.

### Creating an administrative user

By default, no user has permission to perform system administration.
You can give this and other permissions to an existing user by running the following from your terminal in the `skyportal` directory:
```
PYTHONPATH=. python tools/set_user_role.py --username="<username>" --role="<role>"
```

The `role` argument is optional, and defaults to `Super admin`.

You may also list all users and their roles:
```
PYTHONPATH=. python tools/set_user_role.py --list
```


### Test data

By default, SkyPortal contains no data.  You can ingest some sample light curves by running

```
make load_demo_data
```

This also adds `testuser@cesium-ml.org` as an administrator.

### Deploying secure HTTP / SSL certificate

When running a public server, you will likely want to deploy an SSL certificate (i.e., serve `https://your.url` instead of `http://your.url`). Certificates can be obtained for free from services such as Let's Encrypt (https://letsencrypt.org/).

[certbot](https://certbot.eff.org/) is software for helping you obtain a new SSL certificate from Let's Encrypt.
To do so, it first verifies that your server is running (without SSL) at the specified domain.

Start SkyPortal using `make run`.

Then, install `certbot`:
    pip install certbot-nginx

Ask `certbot` to verify the service and retrieve a new certificate:
    sudo certbot certonly --standalone --preferred-challenges http -d http://your.url
or similar if using https
    sudo certbot certonly --standalone --preferred-challenges https -d https://your.url

To renew and retrieve the certificate, do:
    sudo certbot renew

Next, modify the nginx configuration in `baselayer/services/nginx/nginx.conf.template` to use the newly generated certificate, placing it at the top of the server section:

    server {
      listen [::]:443 ssl ipv6only=on;
      listen 443 ssl;
      ssl_certificate /etc/letsencrypt/live/{YOUR_DOMAIN_HERE}/fullchain.pem;
      ssl_certificate_key /etc/letsencrypt/live/{YOUR_DOMAIN_HERE}/privkey.pem;
      include /etc/letsencrypt/options-ssl-nginx.conf;
      ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;
      ...
   }

Finally, stop the app and run it again using `make run`.
