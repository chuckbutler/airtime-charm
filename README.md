# Airtime

Airtime is a simple, open source platform that lets you broadcast streaming
radio on the web.

This charm provides a rapid deployment of a single Airtime host, which bundles a
robust series of services that comprise the application. RabbitMQ, Monit,
Icecast2, Apache2, and the Airtime WebUI + Monitoring components.

# Deploy a Single Stream

    juju deploy airtime
    juju set airtime domain=manage.my.radio


Once installation is complete, you can visit the Airtime installation at the
units public IP, or if you have setup the assigned domain:

    http://manage.my.radio

### Deploy a cluster of streams

    juju deploy airtime
    juju deploy icecast ice-relay
    juju add-relation airtime:scsource ice-relay:screlay

This will deploy the airtime management suite, and deploy a single relay that
will need to be restarted in order to read from the source stream.

    juju run --service ice-relay "service icecast2 restart"

Once installation is complete, you can visit the Airtime installation at the
units public IP, or if you have setup the assigned domain:

    http://manage.my.radio


## Charm Caveats and Issues

Some installations may fail due to PostGRES database not supporting UTF8
encoding.

     pg_dropcluster --stop 9.1 main
     pg_createcluster --start -e UTF-8 9.1 main

# Airtime Configuration

Once deployed the service ships with a default adming user, and pass of `admin`
this exposes an attack vector and should be changed **immediately**

# Upstream Info

## Airtime Project Links

- http://sourcefabric.org/en/airtime
- https://github.com/sourcefabric/Airtime
- http://forum.sourcefabric.org/
