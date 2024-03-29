# Open Education Week - deployment guide

main stuff: see [Upgrade](#upgrade)

## Initial steps

All assuming roughly that we're running Linux (Ubuntu, ...) on all machines involved.

More details about what systems and/or versions are supported/tested:

* Linux: Debian 10, Ubuntu 20.x.x, Fedora 36, 37
* Python: 3.7.x, 3.8.x
* PostgreSQL: 11, 12
* ansible: 5.9.x


### On machine running deployment

Let's call it `machine-a`.

1. have SSH key generated, i.e. `~/.ssh/id_rsa` and `~/.ssh/id_rsa.pub`

2. have `ansible` installed

3. have `oeweek2022` repo checked out

4. have proper content in `<oeweek2 git repo root>/ansible/inventory/dev`
   and `<oeweek2 git repo root>/ansible/inventory/prod` (not part of git repo,
   for security reasons; see `example` or contact colleagues)


### On machine we're deploying to

Let's call it `machine-b`.

1. have SSH machine-a's public SSH key (`~/.ssh/id_rsa.pub`) present in the account under which we're deploying:

   `cat <machine-1 id_rsa.pub> >> .ssh/authorized_keys`

   a. hence you are able to SSH from machine-a to <deploy user>@machine-b without supplying password

2. have SSH key generated, i.e. `~/.ssh/id_rsa` and `~/.ssh/id_rsa.pub`

3. have that public SSH key (`~/.ssh/id_rsa.pub`) added as "Deploy key" on GitLab for the project repo

4. have there a `deployment` deploy branch with local changes need

   * exact steps, changes, etc. - see bellow

5. have the ability to run `supervisorctl restart oerweek-django` without the need to supply password

Some more details, aimed at DEV setup on Ubuntu (PROD setup may be different due to security requirements):


#### for automatic screenshots

As root:

```
apt install libgl1-mesa-glx libxcomposite1 libxrender1 libgstreamer-plugins-base1.0-0
```

And as user running OE Week app:

```
export QT_QPA_PLATFORM=offscreen
```


#### PostgreSQL

As root:

```
apt install postgresql
systemctl enable postgresql.service
systemctl start postgresql.service
```

Still as root, adjust `/etc/postgresql/12/main/pg_hba.conf`:

```
...
# TYPE  DATABASE        USER            ADDRESS                 METHOD
local   oerweek         oerweek                                 password
...
```

As postgres:

```
createuser -W oerweek
createdb -O oerweek oerweek
psql oerweek < dump.sql
```

#### supervisor

As root:

```
apt install supervisor
systemctl enable supervisor.service
systemctl start supervisor.service
```

Still as root replicate following configuration files from PROD and restart the service:

- `/etc/supervisor/conf.d/oerweekapi.conf`
- `/etc/supervisor/conf.d/oerweekapi-q.conf`


#### nginx

TODO


#### certbot

As root:

```
apt install certbot python3-certbot-nginx
certbot --nginx
```


#### localsettings.py

Either do your own based on `localsettings.py.example` or clone and adjust stuff from PROD or DEV server.

Some adjustments are needed, generally regarding hostname, since that is different for DEV site.


## Main stuff

### Backup

TODO


### Upgrade

Example for DEV:

`ansible-playbook -i inventory/dev deploy.yml`


### Rollback

TODO
