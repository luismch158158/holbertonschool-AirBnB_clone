#!/usr/bin/env bash

for f in models/*;do
	echo "#!/usr/bin/python3" > $f
done
