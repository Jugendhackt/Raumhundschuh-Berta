x=0
y=0
z=0
w=1100
a=1
define :musikgenerator do
  if y > w
    play :C4 ,amp:a
  elsif y < -w
    play :D4 ,amp:a
  elsif x > w
    play :E4 ,amp:a
  elsif x < -w
    play :F4 ,amp:a
  elsif z > w
    play :G4 ,amp:a
  elsif z < -w
    play :A4 ,amp:a
  end
end

live_loop :OSCempfang do
  use_real_time
  x,y,z = sync "/osc*/Handschuh/beschleunigung/h"
  musikgenerator
end

live_loop :Entchen do
  use_real_time
  sync "/osc*/Handschuh/Ente"
  allemeineaentchen
end




define :allemeineaentchen do
  play :C4,amp:5,release:1
  sleep 1
  play :D4,amp:5,release:1
  sleep 1
  play :E4,amp:5,release:1
  sleep 1
  play :F4,amp:5,release:1
  sleep 1
  play :G4,amp:5,release:1
  sleep 2
  play :G4,amp:5,release:1
  sleep 2
  play :A4,amp:5,release:1
  sleep 1
  play :A4,amp:5,release:1
  sleep 1
  play :A4,amp:5,release:1
  sleep 1
  play :A4,amp:5,release:1
  sleep 1
  play :G4,amp:5,release:2
  sleep 3
  play :A4,amp:5,release:1
  sleep 1
  play :A4,amp:5,release:1
  sleep 1
  play :A4,amp:5,release:1
  sleep 1
  play :A4,amp:5,release:1
  sleep 1
  play :G4,amp:5,release:2
  sleep 3
  play :F4,amp:5,release:1
  sleep 1
  play :F4,amp:5,release:1
  sleep 1
  play :F4,amp:5,release:1
  sleep 1
  play :F4,amp:5,release:1
  sleep 1
  play :E4,amp:5,release:1
  sleep 2
  play :E4,amp:5,release:1
  sleep 2
  play :G4,amp:5,release:1
  sleep 1
  play :G4,amp:5,release:1
  sleep 1
  play :G4,amp:5,release:1
  sleep 1
  play :G4,amp:5,release:1
  sleep 1
  play :C4,amp:5,release:2
end

