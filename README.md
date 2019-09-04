gabops.papertrail
=================
[![Build Status](https://travis-ci.org/gabops/ansible-role-papertrail.svg?branch=master)](https://travis-ci.org/gabops/ansible-role-papertrail)

Installs and configure papertrail using remote_syslog2 (see 
[Papertrail official documentation](https://help.papertrailapp.com/kb/configuration/configuring-centralized-logging-from-text-log-files-in-unix/)
and [remote_syslog2 Github repo](https://github.com/papertrail/remote_syslog2)

Requirements
------------

None

Role Variables
--------------

| Variable | Value | Description |
| :--- | :--- | :--- |
| papertrail_version | "0.20" | Version to install. 0.20 is the latest at the moment |
| papertrail_config_file_path | /etc/papertrail_conf.yml | Name of the configuration file for remote_syslog |
| papertrail_service_enabled | true | Configure remote_syslog for starting when the system is booted |
| papertrail_service_started | true | The role will start the service after applying the configuration |
| papertrail_managed_conf_file | true | If disabled, no configuration will be applied (None of the following variables will be used). Just the installation so far |
| papertrail_custom_hostname | "" | By default remote_syslog2 uses the hostname of the node. This can be this can be overwritten here |
| papertrail_destination_host | "" | The papertrail destination host to send the logs to. Check your papertrail account for it |
| papertrail_destination_port | "" | The papertrail destination port to connect to the destination host. Check your papertrail account for it |
| papertrail_destination_protocol | tls | This value can be tls(encrypted) or tcp (unencrypted) |
| papertrail_log_facility | "" | The syslog facility to use. See https://en.wikipedia.org/wiki/Syslog#Facility |
| papertrail_log_severity | "" | The syslog severity to use. See https://en.wikipedia.org/wiki/Syslog#Severity_level |
| papertrail_new_file_check_interval | "" | If a glob pattern for logs files is used this parameter controls the frecuency of checking for new log files in the directory |
| papertrail_files_to_log | [] | The file or globs to read |
| papertrail_files_to_exclude | [] | Files to exclude in a directory |
| papertrail_exclude_patterns | [] | The pattern in the log file you are reading you want to ignore. |

> For more detailed information about remote_syslog2 configuration see https://github.com/papertrail/remote_syslog2/blob/master/README.md

> This role also provides the possibility of overwriting any variable in the **vars/** directory. You **never should do it**. This feature only exists for covering any unexpected scenario you might find. For doing it, just declare the variable/variables without the double underscore on your group_vars, host_vars, command line etc as you would do for a variable in defaults/.

Dependencies
------------

None

Example Playbook
----------------

```yaml
    - hosts: servers
      vars:
        papertrail_version: "0.19"
        papertrail_destination_host: logs.papertrailapp.com
        papertrail_destination_port: 12345
        papertrail_custom_hostname: "host-01"
        papertrail_destination_protocol: tls
        papertrail_files_to_log:
          - path: /var/log/httpd.log
            tag: apache
          - /var/log/audit/*.log
          - /var/log/nginx/*.log
        papertrail_files_to_exclude:
          - /var/log/nginx/access.log
        papertrail_log_facility: local7
        papertrail_log_severity: warn
      roles:
         - role: papertrail
```

License
-------

[MIT](./LICENSE)

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops/))
