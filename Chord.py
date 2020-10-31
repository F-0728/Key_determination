import collections

while 1: 
 chord = list(input().split())
 
 bass_line = [chord[i][0] for i in range(len(chord))]
 bass_line2 = [chord[i][0] for i in range(len(chord))]
 
 for i in range(len(chord)):
  try:
   if chord[i][1] == "♭":
    bass_line2[i] += "♭"
   elif chord[i][1] == "♯":
    bass_line2[i] += "♯"
  except:
   pass
 
 
 tone_list = ["C", "D", "E", "F", "G", "A", "B"]
 
 key = []
 
 for i in range(len(bass_line) - 1):
  if tone_list.index(bass_line[i + 1]) == (tone_list.index(bass_line[i]) + 3) % 7:
   if "m" in chord[i + 1]:
    key.append(bass_line2[i + 1] + " Minor")
   else:
    key.append(bass_line2[i + 1] + " Major")
  if tone_list.index(bass_line[i + 1]) == (tone_list.index(bass_line[i]) + 1) % 7:
   if tone_list.index(bass_line[i + 2]) != (tone_list.index(bass_line[i + 1]) + 1) % 7:
    if "m" in chord[i + 1]:
    	key.append(bass_line2[i + 1] + " Minor")
    else:
     key.append(bass_line2[i + 1] + " Major")
 
 
 print("most used:", collections.Counter(key).most_common()[0][0])
 print("ends with:", key[-1])
 
 print()
