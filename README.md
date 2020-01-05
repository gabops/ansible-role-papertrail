gabops.papertrail
=================
[![Build Status](https://travis-ci.org/gabops/ansible-role-papertrail.svg?branch=master)](https://travis-ci.org/gabops/ansible-role-papertrail)

Installs and configures Papertrail (remote_syslog2) (see 
[Papertrail official documentation](https://help.papertrailapp.com/kb/configuration/configuring-centralized-logging-from-text-log-files-in-unix/)
and [remote_syslog2 Github repo](https://github.com/papertrail/remote_syslog2)

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
| papertrail_service_started | true | The role will start the service after applying the configuration. |
| papertrail_managed_conf_file | true | If disabled, no configuration will be applied (None of the following variables will be used). Just the installation and nothing else. |
| papertrail_managed_conf_file_owner | root | Defines the owner of the managed papertrail configuration file. |
| papertrail_managed_conf_file_group | root | Defines the group of the managed papertrail configuration file. |
| papertrail_managed_conf_file_mode | 0644 | Defines the mode of the managed papertrail configuration file. |
| papertrail_managed_conf_file_backup | false | Defines if the role should take a backup of the configuration file before applying any new changes. |
| papertrail_custom_hostname | "" | By default remote_syslog2 uses the hostname of the node. This can be this can be overwritten here. |
| papertrail_destination_host | "" | The papertrail destination host to send the logs to. Check your papertrail account for it. |
| papertrail_destination_port | "" | The papertrail destination port to connect to the destination host. Check your papertrail account for it |
| papertrail_destination_protocol | tls | This value can be tls(encrypted) or tcp (unencrypted). |
| papertrail_log_facility | "" | The syslog facility to use. See https://en.wikipedia.org/wiki/Syslog#Facility |
| papertrail_log_severity | "" | The syslog severity to use. See https://en.wikipedia.org/wiki/Syslog#Severity_level |
| papertrail_new_file_check_interval | "" | If a glob pattern for logs files is used this parameter controls the frecuency of checking for new log files in the directory. |
| papertrail_files_to_log | [] | The file or globs to read. Tipically you will define this variable directly in the playbook. |
| papertrail_files_to_exclude | [] | Files to exclude in a directory. Same as previous `papertrail_files_to_log` but for excluding files to be logged. |
| papertrail_common_files_to_log | [] | Defines common files or globs to read and send to Papertrail. Tipically you will define this variable in the `all` metagroup. |
| papertrail_common_files_to_exclude | [] | Defines common files to exclude. Tipically you will declare this variable in the `all` metagroup. |
| papertrail_group_files_to_log | [] | Defines group files or globs to read and send to Papertrail. Tipically you will define this variable in any of the groups your inventory (e.g. group_vars/webservers/). |
| papertrail_group_files_to_exclude | [] | Defines files to exlude per group. Same as previous `papertrail_group_files_to_log` but for excluding files to be logged. |
| papertrail_host_files_to_log | [] | Defines host files or globs to read and send to Papertrail. Tipically you will define this in a host_vars file (e.g. host_vars/host-01/). |
| papertrail_host_files_to_exclude | [] | Defines files to exlude per host. Same as previous `papertrail_host_files_to_log` but for excluding files to be logged. |
| papertrail_exclude_patterns | [] | The patterns in the log file you are reading you want to ignore. |

> For more detailed information about remote_syslog2 configuration see https://github.com/papertrail/remote_syslog2/blob/master/README.md

Dependencies
------------

None.

Example Playbook
----------------

- group_vars/all/papertrail.yml:
```yaml
papertrail_common_files_to_log:
  - path: /var/log/messages
    tag: messages
  - path: /var/log/secure
    tag: secure
```

- group_vars/webservers/papertrail.yml:
```yaml
papertrail_group_files_to_log:
  - path: /var/log/httpd.log
    tag: apache
```

- host_vars/host-01/papertrail.yml:
```yaml
papertrail_custom_hostname: "problematic-host-01"
papertrail_host_files_to_log:
  - /var/log/dmesg
```

- playbook.yml
```yaml
- hosts: servers
  vars:
    papertrail_version: "0.19"
    papertrail_destination_host: logs.papertrailapp.com
    papertrail_destination_port: 12345
    papertrail_destination_protocol: tls
    papertrail_log_facility: local7
    papertrail_log_severity: warn
    papertrail_managed_conf_file_backup: true
    papertrail_files_to_log:
      - /var/log/audit/audit.log
    
  roles:
      - role: papertrail
```

License
-------

[MIT](./LICENSE)

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops/))
