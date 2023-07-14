import time
for h in range(24):
  for min in range(59):
    for sec in range(59):
      print(h,":",min,":",sec)
      time.sleep(1)
