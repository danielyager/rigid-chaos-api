from views import bp

@bp.route("/mailing/add")
def add_person_to_mailing_list():
    return "We have added someone to the mailing list!"

@bp.route("/mailing/remove")
def remove_person_from_mailing_list():
    return "We have removed someone from the mailing list!"

@bp.route("/mailing/verify-email")
def verify_email():
    return "We are verifying a person's email!"

@bp.route("/mailing/send-mass-email")
def send_mass_email():
    return "We are sending an email to all verified subscribers!"