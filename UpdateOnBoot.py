import apt
import os

if os.geteuid() == 0:
    print("Checking for updates")
    
    cache = apt.Cache()

    cache.update()

    cache.upgrade(True)

    changes = cache.get_changes()

    if len(changes) > 0:
        for pkg in changes:
            print(f"Aktualisierung verfügbar: {pkg}")
        print("UPDATING")
        #cache.autoremove()
        cache.commit()
        print("Updates finished -- REBOOTING")
        os.system('sytemctl reboot')
    else:
        print("No Updates -- BOOTING")
else:
    raise Exception("NO SUPERUSER PRIVILEGES")
