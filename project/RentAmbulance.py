from inputdata import inputdata
import Tampilan 
import AmbulanceTersedia


def RentAmbulance():
  try:
    # Dapatkan input jenis mobil ambulans yang dipilih 
    ambulance = int(input("\nMasukkan jenis mobil ambulans (1/2): "))    
    if (ambulance == 1):
        ambulance_type = "Mobil Ambulans Umum"
        Tampilan.Tampilan.ambulance_rate = 500000
        inputdata(Tampilan.Tampilan.ambulance_rate)
    elif (ambulance == 2):
        ambulance_type = "Mobil Ambulans Gabungan"
        Tampilan.Tampilan.ambulance_rate = 1000000
        inputdata(Tampilan.Tampilan.ambulance_rate)
    else:
        print("Jenis mobil ambulans tidak valid")        
        print("pilihan invalid masukkan pilihan hanya 1 / 2!")
        AmbulanceTersedia.AmbulanceTersedia()
  except:
    print("pilihan invalid masukkan pilihan hanya 1 / 2!")
        AmbulanceTersedia.AmbulanceTersedia()
