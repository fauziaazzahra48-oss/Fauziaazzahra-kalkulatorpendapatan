from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    rata_rata = None
    if request.method == 'POST':
        try:
            # Ambil data dari form HTML
            total_pendapatan = float(request.form.get('total_pendapatan'))
            jumlah_bulan = int(request.form.get('jumlah_bulan'))
            
            if jumlah_bulan > 0:
                # Logika perhitungan
                hasil = total_pendapatan / jumlah_bulan
                # Format ke Rupiah
                rata_rata = "Rp {:,.0f}".format(hasil).replace(",", ".")
        except (ValueError, TypeError):
            rata_rata = "Input tidak valid"

    return render_template('index.html', hasil=rata_rata)

if __name__ == '__main__':
    app.run(debug=True)