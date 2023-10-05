sed -i -e"s/^max_connections = 100.*$/max_connections = 1000/" /var/lib/postgresql/data/postgresql.conf
sed -i -e"s/^shared_buffers =.*$/shared_buffers = 2GB/" /var/lib/postgresql/data/postgresql.conf
sed -i -e"s/^#effective_cache_size = 128MB.*$/effective_cache_size = 4GB/" /var/lib/postgresql/data/postgresql.conf
sed -i -e"s/^#work_mem = 1MB.*$/work_mem = 16MB/" /var/lib/postgresql/data/postgresql.conf
sed -i -e"s/^#maintenance_work_mem = 16MB.*$/maintenance_work_mem = 1GB/" /var/lib/postgresql/data/postgresql.conf
sed -i -e"s/^#checkpoint_segments = .*$/checkpoint_segments = 32/" /var/lib/postgresql/data/postgresql.conf
sed -i -e"s/^#checkpoint_completion_target = 0.5.*$/checkpoint_completion_target = 0.7/" /var/lib/postgresql/data/postgresql.conf
sed -i -e"s/^#wal_buffers =.*$/wal_buffers = 16MB/" /var/lib/postgresql/data/postgresql.conf
sed -i -e"s/^#default_statistics_target = 100.*$/default_statistics_target = 100/" /var/lib/postgresql/data/postgresql.conf

cp /pg_hba.conf /var/lib/postgresql/data/pg_hba.conf
