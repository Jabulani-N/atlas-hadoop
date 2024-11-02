# atlas-hadoop
A repository that demonstrates Hadoop

# Installation

[How to Install Hadoop 3 on Ubuntu – A Step-by step Installation Process](https://data-flair.training/blogs/installation-of-hadoop-3-on-ubuntu/)

[How to Install and Configure Hadoop on Ubuntu 20.04](https://tecadmin.net/install-hadoop-on-ubuntu-20-04/)

[Hadoop: Setting up a Single Node Cluster](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/SingleCluster.html)


I installed following [this tutoprial](https://www.youtube.com/watch?v=ZnrtnFEz22E)

I begin running with:
1. sudo service ssh start
1. ssh localhost
1. /mnt/d/Apps/Container/Hadoop/hadoop-3.3.6/sbin/start-all.sh
and end with:
* /mnt/d/Apps/Container/Hadoop/hadoop-3.3.6/sbin/stop-all.sh
yours will take place in your own Hadoop directory, so the only part I expect to be the same on your own machine are `/hadoop-3.3.6/sbin/start-all.sh` and `/hadoop-3.3.6/sbin/stop-all.sh`

## Troubleshooting

Connectoin Refused

`localhost:9000 failed on connection exception: java.net.ConnectException: Connection refused; For more details see:  http://wition: java.net.ConnectExki.apache.org/hadoop/ConnectionRefused`

* doublecheck your `hdfs-site.xml` file and be sure it contains

```

<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>

```

* be certain you have run
  1. `sudo service ssh start`
  2. `ssh localhost`
  3. `Address Here/sbin/start-all.sh`
      * It seems to be a need to do this each login/restart of the machine
      * if you have run the `stop` version, you only need to perform the `start` again, rather than all hte steps before, after they've been run once.
