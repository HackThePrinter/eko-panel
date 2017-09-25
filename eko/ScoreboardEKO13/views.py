from django.shortcuts import render
from .models import Name, ExploitType, Vuln, Exploit
from datetime import datetime


def index(request):
    vulns_found = Vuln.objects.count()

    vulns_exploited = Exploit.objects.count()

    today_start = int(
        datetime.strptime(
            datetime.today().strftime('%Y-%m-%d'),
            '%Y-%m-%d'
        ).timestamp()
    )
    today_end = today_start + 24 * 3600
    vuln_first_today = Vuln.objects.filter(
        timestamp__gte=today_start,
        timestamp__lt=today_end,
    ).prefetch_related()[0]

    exploit_first_today = Exploit.objects.filter(
        timestamp__gte=today_start,
        timestamp__lt=today_end
    ).prefetch_related()[0]

    # Dude, what the fuck is this!?
    vulns_top = [{'name': 'alfred', 'qty': 2}, {'name': 'ivan', 'qty': 1}]  # Vuln.objects.raw("select t1.id, t1.name, (select count(id) from ScoreboardEKO13_vuln as t2 where t1.id = t2.name_id) as 'qty' from ScoreboardEKO13_name as t1 order by qty desc limit 5")

    vulns_latest = Vuln.objects.raw('SELECT 1 AS id, * FROM (SELECT name, timestamp FROM "ScoreboardEKO13_vuln" INNER JOIN "ScoreboardEKO13_name" on "ScoreboardEKO13_vuln".name_id = "ScoreboardEKO13_name".id WHERE "timestamp" >= 1506308400 AND "timestamp" < 1506394800 UNION SELECT name, timestamp FROM "ScoreboardEKO13_exploit" INNER JOIN "ScoreboardEKO13_name" on "ScoreboardEKO13_exploit".name_id = "ScoreboardEKO13_name".id WHERE "timestamp" >= 1506308400 AND "timestamp" < 1506394800) ORDER BY timestamp DESC')  # Vuln.objects.order_by('-timestamp')[:5]

    context = {
        'vulns_top': vulns_top,
        'vulns_latest': vulns_latest,
        'vulns_found': vulns_found,
        'vulns_exploited': vulns_exploited,
        'vuln_first_today': vuln_first_today,
        'exploit_first_today': exploit_first_today,
    }
    return render(request, 'ScoreboardEKO13/index.html', context)
