# Certbot plugin for authentication using Gandi LiveDNS

This is a plugin for [Certbot](https://certbot.eff.org/) that uses the Gandi
LiveDNS API to allow [Gandi](https://www.gandi.net/)
customers to prove control of a domain name. This is an alteration of that
produced by Michael Porter and Yohann Leon allowing the user to store API 
details using AWS System Manager (Parameter Store).

## Usage

1. Obtain a Gandi API token (see [Gandi LiveDNS API](https://doc.livedns.gandi.net/))

2. Install the plugin using `pip install certbot-plugin-gandi-aws`

3. Create AWS parameters for the following contents (see [AWS Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)):

   * API key
   * Sharing ID  - optional (Organisation ID)

4. Set an environment variables referencing the parameter names used to store
   the Gandi content.

   ```commandline
   export GANDI_API_REF=<aws_gandi_api_parameter>
   export GANDI_SHARING_REF=<aws_gandi_sharing_parameter>
   ```
   
   Replace the `<aws_gandi_api_parameter>` with the name of the parameter used
   to store your Gandi API Key. 

   Replace the `<aws_gandi_sharing_parameter>` with the name of the parameter
   used to store your Gandi Sharing ID.

6. Run `certbot` and direct it to use the plugin for authentication and to use
   the config file previously created:
   ```
   certbot certonly --authenticator dns-gandi -d domain.com
   ```
   Add additional options as required to specify an installation plugin etc.

Please note that this solution is usually not relevant if you're using Gandi's web hosting services as Gandi offers free automated certificates for all simple hosting plans having SSL in the admin interface.

Be aware that the plugin configuration must be provided by CLI, configuration for third-party plugins in `cli.ini` is not supported by certbot for the moment. Please refer to [#4351](https://github.com/certbot/certbot/issues/4351), [#6504](https://github.com/certbot/certbot/issues/6504) and [#7681](https://github.com/certbot/certbot/issues/7681) for details.

## Distribution

PyPI is the upstream distribution channel.

* PyPI: https://pypi.org/project/certbot-plugin-gandi-aws/

Every release pushed to PyPI is signed with GPG.

## Wildcard certificates

This plugin is particularly useful when you need to obtain a wildcard certificate using dns challenges:

```
certbot certonly --authenticator dns-gandi -d domain.com -d \*.domain.com --server https://acme-v02.api.letsencrypt.org/directory
```

## Automatic renewal

You can setup automatic renewal using `crontab` with the following job for weekly renewal attempts:

```
0 0 * * 0 certbot renew -q --authenticator dns-gandi --server https://acme-v02.api.letsencrypt.org/directory
```

## FAQ

> I have a warning telling me `Plugin legacy name certbot-plugin-gandi:dns may be removed in a future version. Please use dns instead.`

Certbot had moved to remove 3rd party plugins prefixes since v1.7.0. Please switch to the new configuration format and remove any used prefix-based configuration.
For the time being, you can still use prefixes, but if you do so and keep using prefix-based cli arguments, stay consistent and use prefix-based configuration in the ini file.

> I get a `Property "certbot_plugin_gandi:dns_api_key" not found (should be API key for Gandi account).. Skipping.`

See above.

> Why do you keep this plugin a third-party plugin ? Just merge it with certbot ?

This Gandi plugin is a third party plugin mainly because this plugin is not officially backed by Gandi and because Certbot [does not accept](https://certbot.eff.org/docs/contributing.html?highlight=propagation#writing-your-own-plugin) new plugin submissions.

![no_submission](https://user-images.githubusercontent.com/2095991/101479748-fd9da280-3952-11eb-884f-491470718f4d.png)

## Credits

Huge thanks to Michael Porter and Yohann Leon for their [original work](https://github.com/obynio/certbot-plugin-gandi) !
