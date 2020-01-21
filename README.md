gabops.papertrail
=================
[![Build Status](https://travis-ci.org/gabops/ansible-role-papertrail.svg?branch=master)](https://travis-ci.org/gabops/ansible-role-papertrail)

Installs and configures Papertrail (remote_syslog2).

Requirements
------------

None.

Role Variables
--------------

| Variable | Value | Description |
| :--- | :--- | :--- |
| papertrail_version | "0.20" | Version to install. 0.20 is the latest at the moment. |
| papertrail_config_file_path | /etc/papertrail_conf.yml | Name of the configuration file for remote_syslog. |
| papertrail_service_enabled | true | Configure remote_syslog for starting when the system is booted. |
| papertrail_service_state | started | Defines the status of the service. |
| papertrail_managed_conf_file | true | If false, no configuration will be applied (All variables below will be ignored). Just the installation and nothing else. |
| papertrail_custom_hostname | "" | By default remote_syslog2 uses the hostname of the node. This can be this can be overwritten here. |
| papertrail_destination_host | "" | Defines the Papertrail destination host to send the logs to. Check your papertrail account for it. |
| papertrail_destination_port | "" | Defines the Papertrail destination port to connect to the destination host. Check your papertrail account for it |
| papertrail_destination_protocol | tls | This value can be tls(encrypted) or tcp (unencrypted). |
| papertrail_log_facility | "" | The Syslog facility to use. See https://en.wikipedia.org/wiki/Syslog#Facility |
| papertrail_log_severity | "" | The Syslog severity to use. See https://en.wikipedia.org/wiki/Syslog#Severity_level |
| papertrail_new_file_check_interval | "" | If a glob pattern for logs files is used this parameter controls the frecuency of checking for new log files in the directory. |
| papertrail_files_to_log | [] | The file or globs to read. |
| papertrail_files_to_exclude | [] | Files to exclude in a directory. |
| papertrail_exclude_patterns | [] | The pattern in the log file you are reading you want to ignore. |


> For more detailed information about remote_syslog2 configuration please visit [remote_syslog2 documentation](https://github.com/papertrail/remote_syslog2/blob/master/README.md) on Github.

> For more detailed information about Papertrail please visit
[official documentation](https://help.papertrailapp.com/kb/configuration/configuring-centralized-logging-from-text-log-files-in-unix/)

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: webserver-01
  vars:
    papertrail_version: "0.19"
    papertrail_destination_host: logs.papertrailapp.com
    papertrail_destination_port: 12345
    papertrail_destination_protocol: tls
    papertrail_log_facility: local7
    papertrail_log_severity: warn
    papertrail_custom_hostname: "main-server-01"
    papertrail_files_to_log:
      - path: /var/log/messages
        tag: messages
      - /var/log/dmesg
      - /var/log/httpd/access_log
    papertrail_exclude_patterns:
      - ^password.*
    papertrail_exclude_files:
      - .tar.gz
      - "*.old"
  roles:
      - role: papertrail
```

License
-------

[MIT](./LICENSE)

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops/))
