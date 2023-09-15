OFFICES = {
    'βασιλας': 'Κ16.115',
    'γαλιωτου': 'Κ16.122',
    'γεωργουλη': 'Κ16.216',
    'γιαννακοπουλος': 'Στο διαδρομο του εργαστηριου SUN',
    'διλιντας': 'Κ16.203',
    'ελληνας': 'Κ16.203',
    'καρανικολας': 'Κ16.120',
    'κεχαγιας': 'Κ16.116',
    'κουκουλετσος': 'Κ16.204',
    'μαγος': 'Κ16.119',
    'μαμαλης': 'Κ16.120-121',
    'μαστοροκωστας': 'Κ16.204',
    'μιαουλης': 'Κ16.118',
    'νικολοπουλος': 'Στο διαδρομο του εργαστηριου SUN',
    'παντζιου': 'Κ16.115',
    'πρεζερακος': 'Κ16.203',
    'σαμαρακου': 'Κ16.208',
    'σγουροπουλου': 'Κ16.123',
    'σκουρλας': 'Κ16.120-121',
    'χαλαρης': 'Κ16.120-121',
    'μπογρης': 'Κ16.999',
    'φατουρος': 'Κ16.204',
    'βουλοδημος': 'Κ16.118',
    'καντζαβελου': 'Κ16.122',
    'καρκαζης': 'Κ16.203',
    'κουμπουρος': 'Κ16.122',
    'ξυδας': 'Κ16.120-121',
    'μπαρδης': 'Κ16.199',
    'βελωνη': 'Κ16.204',
    'γεωργουλακη': 'Κ16.999',
    'μελετιου': 'K10.018',
    'γιαλπας': 'Κ16.121',
    'παυλιδης': 'Κ16.ΚΔΕ',
    'κάβουρας': 'Κ11.132',
    'κανδαράκης': 'Κ10.122',
    'σπυρόπουλος': 'Κ11.130',
    'ασβεστάς': 'Κ11.131',
    'βαλαής': 'Κ11.138-139',
    'βεντούρας': 'Κ16.107',
    'γκλώτσος': 'Κ11.132',
    'καλατζής': 'Κ11.131',
    'καλλέργη': 'Κ11.110-129',
    'ντούνης': 'Κ10.027-026',
    'πατσαβούδη': 'Κ16.108',
    'σκουρολιάκου': 'Κ11.103',
    'φούντος': 'Κ10.123-121-039',
    'καλύβας': 'Κ11.105',
    'κωστόπουλος': 'Κ11.132',
    'λιαπαρίνος': 'Κ11.105',
    'μουστάνης': 'Κ10.027',
    'αθανασιάδης': 'Κ11.132',
    'δαυίδ': 'Κ11.107',
    'ματσούκας': 'Κ11.109',
    'μιχαήλ': 'Κ11.139',
    'παντατοσάκη': 'Κ11.106',
    'κορκίδης': 'K10.027'
}

HOURS = 18000  # 5 hours to secs
ANNOUNCE_CHN_ID = int(open('data/CHANNEL_ID.txt', 'r').readline().strip())
URL = [
        "http://www.ice.uniwa.gr/announcements-all/"
        "https://bme.uniwa.gr/category/announcements/"
        "https://idpe.uniwa.gr/news/department"
        "https://www.uniwa.gr/category/announcements/"
]
AOC_JOIN = open('data/aoc_join.txt', 'r').readline().strip()
AOC_ID = AOC_JOIN.split("-")[0]
AOC_SESSION = open("data/aoc_session.txt", "r").readline().strip()