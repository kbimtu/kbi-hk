# Restore corrupted V3 pages from V2 backup with path fixes
$ErrorActionPreference = 'Stop'
$v2 = "c:\Users\katep\OneDrive\GoodNotes\Desktop\KBI Related Development\KBI HK Website V2 (Without Translation)"
$v3 = "c:\Users\katep\OneDrive\GoodNotes\Desktop\KBI Related Development\KBI HK Website V3 (With Translation)"

function Transform-Html([string]$html, [string]$zone) {
    $html = $html -replace '\\', '/'
    switch ($zone) {
        'programme' {
            $html = $html -replace 'href="kbi-hk\.css"', 'href="../kbi-hk.css"'
            $html = $html -replace 'src="kbi-hk\.js"', 'src="../kbi-hk.js"'
            $html = $html -replace 'href="index\.html"', 'href="../index.html"'
            $html = $html -replace 'href="about-', 'href="../about/about-'
            $html = $html -replace 'href="media\.html"', 'href="../media.html"'
            $html = $html -replace 'href="contact\.html"', 'href="../contact.html"'
            $html = $html -replace 'href="faq\.html"', 'href="../faq.html"'
            $html = $html -replace 'href="impact\.html"', 'href="../about/about-impact.html"'
            $html = $html -replace 'href="events\.html"', 'href="../upcoming events/events.html"'
            $html = $html -replace 'href="eto2026\.html"', 'href="../upcoming events/eto2026.html"'
            $html = $html -replace 'href="news(\d*)\.html"', 'href="../news/news$1.html"'
            $html = $html -replace 'href="event(\d+)\.html"', 'href="../upcoming events/event$1.html"'
            $html = $html -replace 'href="programmes\.html"', 'href="programmes.html"'
        }
        'news' {
            $html = $html -replace 'href="kbi-hk\.css"', 'href="../kbi-hk.css"'
            $html = $html -replace 'src="kbi-hk\.js"', 'src="../kbi-hk.js"'
            $html = $html -replace 'href="index\.html"', 'href="../index.html"'
            $html = $html -replace 'href="about-', 'href="../about/about-'
            $html = $html -replace 'href="media\.html"', 'href="../media.html"'
            $html = $html -replace 'href="contact\.html"', 'href="../contact.html"'
            $html = $html -replace 'href="faq\.html"', 'href="../faq.html"'
            $html = $html -replace 'href="events\.html"', 'href="../upcoming events/events.html"'
            $html = $html -replace 'href="eto2026\.html"', 'href="../upcoming events/eto2026.html"'
            $html = $html -replace 'href="news(\d*)\.html"', 'href="news$1.html"'
            $html = $html -replace 'href="event(\d+)\.html"', 'href="../upcoming events/event$1.html"'
            $html = $html -replace 'href="competitions\.html"', 'href="../programme/competitions.html"'
            $html = $html -replace 'href="certifications\.html"', 'href="../programme/certifications.html"'
            $html = $html -replace 'href="collaborations\.html"', 'href="../programme/collaborations.html"'
            $html = $html -replace 'href="projects\.html"', 'href="../programme/projects.html"'
            $html = $html -replace 'href="community\.html"', 'href="../programme/community.html"'
            $html = $html -replace 'href="membership\.html"', 'href="../programme/membership.html"'
            $html = $html -replace 'href="sponsors\.html"', 'href="../programme/sponsors.html"'
            $html = $html -replace 'href="scholarships\.html"', 'href="../programme/scholarships.html"'
            $html = $html -replace 'href="sisters\.html"', 'href="../programme/sisters.html"'
        }
        'events' {
            $html = $html -replace 'href="kbi-hk\.css"', 'href="../kbi-hk.css"'
            $html = $html -replace 'src="kbi-hk\.js"', 'src="../kbi-hk.js"'
            $html = $html -replace 'href="index\.html"', 'href="../index.html"'
            $html = $html -replace 'href="about-', 'href="../about/about-'
            $html = $html -replace 'href="media\.html"', 'href="../media.html"'
            $html = $html -replace 'href="contact\.html"', 'href="../contact.html"'
            $html = $html -replace 'href="faq\.html"', 'href="../faq.html"'
            $html = $html -replace 'href="news(\d*)\.html"', 'href="../news/news$1.html"'
            $html = $html -replace 'href="event(\d+)\.html"', 'href="event$1.html"'
            $html = $html -replace 'href="events\.html"', 'href="events.html"'
            $html = $html -replace 'href="eto2026\.html"', 'href="eto2026.html"'
            $html = $html -replace 'href="competitions\.html"', 'href="../programme/competitions.html"'
            $html = $html -replace 'href="certifications\.html"', 'href="../programme/certifications.html"'
            $html = $html -replace 'href="collaborations\.html"', 'href="../programme/collaborations.html"'
            $html = $html -replace 'href="projects\.html"', 'href="../programme/projects.html"'
            $html = $html -replace 'href="community\.html"', 'href="../programme/community.html"'
            $html = $html -replace 'href="membership\.html"', 'href="../programme/membership.html"'
            $html = $html -replace 'href="sponsors\.html"', 'href="../programme/sponsors.html"'
            $html = $html -replace 'href="scholarships\.html"', 'href="../programme/scholarships.html"'
            $html = $html -replace 'href="sisters\.html"', 'href="../programme/sisters.html"'
        }
        'about' {
            $html = $html -replace 'href="kbi-hk\.css"', 'href="../kbi-hk.css"'
            $html = $html -replace 'src="kbi-hk\.js"', 'src="../kbi-hk.js"'
            $html = $html -replace 'href="index\.html"', 'href="../index.html"'
            $html = $html -replace 'href="media\.html"', 'href="../media.html"'
            $html = $html -replace 'href="contact\.html"', 'href="../contact.html"'
            $html = $html -replace 'href="faq\.html"', 'href="../faq.html"'
            $html = $html -replace 'href="events\.html"', 'href="../upcoming events/events.html"'
            $html = $html -replace 'href="eto2026\.html"', 'href="../upcoming events/eto2026.html"'
            $html = $html -replace 'href="news(\d*)\.html"', 'href="../news/news$1.html"'
            $html = $html -replace 'href="impact\.html"', 'href="about-impact.html"'
            $html = $html -replace 'href="competitions\.html"', 'href="../programme/competitions.html"'
            $html = $html -replace 'href="certifications\.html"', 'href="../programme/certifications.html"'
            $html = $html -replace 'href="collaborations\.html"', 'href="../programme/collaborations.html"'
            $html = $html -replace 'href="projects\.html"', 'href="../programme/projects.html"'
            $html = $html -replace 'href="community\.html"', 'href="../programme/community.html"'
            $html = $html -replace 'href="membership\.html"', 'href="../programme/membership.html"'
            $html = $html -replace 'href="sponsors\.html"', 'href="../programme/sponsors.html"'
            $html = $html -replace 'href="scholarships\.html"', 'href="../programme/scholarships.html"'
            $html = $html -replace 'href="sisters\.html"', 'href="../programme/sisters.html"'
            $html = $html -replace 'href="event-gallery-', 'href="../event gallery/event-gallery-'
            $html = $html -replace 'src="images/', 'src="../event gallery/images/'
        }
        'gallery' {
            $html = $html -replace 'href="kbi-hk\.css"', 'href="../kbi-hk.css"'
            $html = $html -replace 'href="index\.html"', 'href="../index.html"'
            $html = $html -replace 'href="about-', 'href="../about/about-'
            $html = $html -replace 'href="media\.html"', 'href="../media.html"'
            $html = $html -replace 'href="contact\.html"', 'href="../contact.html"'
            $html = $html -replace 'href="faq\.html"', 'href="../faq.html"'
            $html = $html -replace 'href="news(\d*)\.html"', 'href="../news/news$1.html"'
            $html = $html -replace 'href="events\.html#past-events"', 'href="../about/about-history.html#archive"'
            $html = $html -replace 'href="events\.html"', 'href="../upcoming events/events.html"'
            $html = $html -replace 'href="eto2026\.html"', 'href="../upcoming events/eto2026.html"'
            $html = $html -replace 'href="competitions\.html"', 'href="../programme/competitions.html"'
            $html = $html -replace 'href="certifications\.html"', 'href="../programme/certifications.html"'
            $html = $html -replace 'href="collaborations\.html"', 'href="../programme/collaborations.html"'
            $html = $html -replace 'href="projects\.html"', 'href="../programme/projects.html"'
            $html = $html -replace 'href="community\.html"', 'href="../programme/community.html"'
            $html = $html -replace 'href="membership\.html"', 'href="../programme/membership.html"'
            $html = $html -replace 'href="sponsors\.html"', 'href="../programme/sponsors.html"'
            $html = $html -replace 'href="scholarships\.html"', 'href="../programme/scholarships.html"'
            $html = $html -replace 'href="sisters\.html"', 'href="../programme/sisters.html"'
            $html = $html -replace 'src="images/', 'src="images/'
            # Replace inline lightbox script with kbi-hk.js
            $html = $html -replace '(?s)  <script>\s*const hamburger.*?  </script>\s*</body>', "  <script src=`"../kbi-hk.js`"></script>`n</body>"
        }
    }
    return $html
}

function Copy-Transformed($srcFile, $destFile, $zone) {
    $html = Get-Content -LiteralPath $srcFile -Raw -Encoding UTF8
    $html = Transform-Html $html $zone
    $dir = Split-Path $destFile -Parent
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
    [System.IO.File]::WriteAllText($destFile, $html, [System.Text.UTF8Encoding]::new($false))
    Write-Host "Restored: $destFile"
}

# Programme pages
@('competitions','certifications','collaborations','community','membership','projects','programmes','scholarships','sisters','sponsors') | ForEach-Object {
    Copy-Transformed "$v2\$_.html" "$v3\programme\$_.html" 'programme'
}

# News
Copy-Transformed "$v2\news.html" "$v3\news\news.html" 'news'
1..8 | ForEach-Object { Copy-Transformed "$v2\news$_.html" "$v3\news\news$_.html" 'news' }

# Upcoming events
Copy-Transformed "$v2\events.html" "$v3\upcoming events\events.html" 'events'
Copy-Transformed "$v2\eto2026.html" "$v3\upcoming events\eto2026.html" 'events'
1..15 | ForEach-Object { Copy-Transformed "$v2\event$_.html" "$v3\upcoming events\event$_.html" 'events' }

# About (keep V3 about-history; restore others)
@('about-impact','about-team','about-who-we-are') | ForEach-Object {
    Copy-Transformed "$v2\$_.html" "$v3\about\$_.html" 'about'
}
Copy-Transformed "$v2\impact.html" "$v3\about\impact.html" 'about'
if (Test-Path "$v2\about.html") { Copy-Transformed "$v2\about.html" "$v3\about\about.html" 'about' }

# Event galleries (skip 2021 — keep V3 version)
@('2018','2019','2020','2022','2023','2024','2025') | ForEach-Object {
    Copy-Transformed "$v2\event-gallery-$_.html" "$v3\event gallery\event-gallery-$_.html" 'gallery'
}

Write-Host 'Done.'
