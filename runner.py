import ansible_runner
r = ansible_runner.run(private_data_dir='/home/devasc/ansible_project', playbook='playbook.yaml')
print("{}: {}".format(r.status, r.rc))
# successful: 0
for each_host_event in r.events:
    print(each_host_event['event'])
print("Final status:")
print(r.stats)
