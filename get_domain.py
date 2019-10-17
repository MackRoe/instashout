class DomainSMS:
    def assign_domain(self, contact_provider):
        if profile.contact_provider == "Verizon":
            provider_domain = "vtext.com"
        elif profile.contact_provider == "Alltel":
            provider_domain = "message.alltel.com"
        elif profile.contact_provider == "AT&T":
            provider_domain = 'txt.att.net'
        elif profile.contact_provider == "T-Mobile":
            provider_domain = "tmomail.net"
        elif profile.contact_provider == "Virgin Mobile":
            provider_domain = "vmobl.com"
        elif profile.contact_provider == "Sprint":
            provider_domain = "messaging.sprintpcs.com"
        elif profile.contact_provider == "Nextel":
            provider_domain = "messaging.nextel.com"
        elif profile.contact_provider == "USCellular":
            provider_domain = "mms.uscc.net"
        else:
            provider_domain = None
        return provider_domain