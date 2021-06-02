pengeluaran_sewa_dokter = 35000
pendapatan_dari_customer = 50000
pendapatan_dari_vitamin = 50000
vitamin = 20000
delivery_vitamin = 10000
packaging_vitamin = 3000
pengeluaran_untuk_produksi_vitamin = vitamin + delivery_vitamin + packaging_vitamin
month= ['October', 'November', 'December']
session_dokter= [112897, 116898, 147559]
session_vitamin = [21897,23898,27559]
revenue = [0,0,0]
cogs = [0,0,0]
biaya_produksi_vitamin = [0,0,0]
biaya_sewa_dokter = [0,0,0]
biaya_pendapatan_dari_customer = [0,0,0]
biaya_pendapatan_dari_vitamin = [0,0,0]
depreciation_october_and_november = 12500000 * 2
five_years = 5 * 12
harga_laptop = 10000000
biaya_depreciation_laptop_5pcs_in_10years_per_one_month =  harga_laptop / five_years
income_loss = [0,0,0]
depreciation_october_or_november = 12500000


expenses = [0,0,0 ]
expenses[0] = depreciation_october_or_november + 353050000
expenses[1] = depreciation_october_or_november + 353050000
expenses[2] = biaya_depreciation_laptop_5pcs_in_10years_per_one_month + 368900000

other_income = [120000, 189000,1250000]
#tax daro october to december sama
tax = 57000

for i in range(3):
    biaya_produksi_vitamin[i] = pengeluaran_untuk_produksi_vitamin * session_vitamin[i]
    biaya_pendapatan_dari_vitamin[i]= pendapatan_dari_vitamin * session_vitamin[i]
    biaya_pendapatan_dari_customer[i]= pendapatan_dari_customer * session_dokter[i]
    biaya_sewa_dokter[i] = pengeluaran_sewa_dokter * session_dokter[i]

    revenue[i] = biaya_pendapatan_dari_vitamin[i] + biaya_pendapatan_dari_customer[i]
    cogs[i] = biaya_produksi_vitamin[i] + biaya_sewa_dokter[i]

    income_loss[i] = revenue[i] + other_income[i] - cogs[i] - expenses[i] - tax
    print("{}. {} : {}".format(i+1, month[i], income_loss[i]))

# hasil akhir = October - Rp  1,700,217,000; November - Rp 1,794,318,000 ; December - Rp 2,314,014,333.33

# Soal
# Find the transactions of PT ABC as follows:

# 1. Customers need to pay IDR 50.000 for every online consultation session with a doctor. PT ABC will pay the doctor for IDR 35,000 per session

# "2. Number of session bookings made per month are as follows: 
# Oct (112,897) - Nov (116,898) - Dec (147,559)"

# 3. One package of immune booster vitamin is IDR 50,000/ package . The vitamin cost per package is IDR 20,000 + delivery fee of IDR 10,000 and packaging fee of IDR 3,000

# 4. Number of vitamin packages sold each month: Oct (21,897) - Nov (23,898) - Dec (27,559)

# "5. On October & November 2020, total depreciation costs are IDR 12,500,000 per month. In December, there are 5 new members joining the company and PT ABC bought 5 new laptops that cost IDR 10,000,000 each and has lifetime value of 5 years. 

# Let's assume that the company is adopting straightline depreciation method and the December depreciation calculation = November depreciation + Depreciation of Purchase of the 5 laptops in December."

# 6. Determine the net income/loss of PT ABC from October to December.

# We have provided the formula to help you quickly determine the net profit or loss in each cell. There is no need to change the formulas in the cells.