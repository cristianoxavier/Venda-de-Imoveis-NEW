from server import db, ma


class tb_proprietario(db.Model):

    id_proprietario = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    nm_proprietario = db.Column(db.String)
    cpf_proprietario = db.Column(db.String)
    rg_proprietario = db.Column(db.String)
    data_nascimento = db.Column(db.Date)
    estado_civil = db.Column(db.String)
    profissao = db.Column(db.String)

class ProprietarioSchema(ma.ModelSchema):
    class Meta:
        fields = (
            "id_proprietario",
            "nm_proprietario",
            "cpf_proprietario",
            "rg_proprietario",
            "data_nascimento",
            "data_nascimento",
            "estado_civil",
            "profissao"
        )
