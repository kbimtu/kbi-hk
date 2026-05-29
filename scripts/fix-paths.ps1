$v3 = "c:\Users\katep\OneDrive\GoodNotes\Desktop\KBI Related Development\KBI HK Website V3 (With Translation)"

function Fix-File($path, [scriptblock]$fn) {
    if (-not (Test-Path $path)) { return }
    $html = [System.IO.File]::ReadAllText($path)
    $orig = $html
    $html = & $fn $html
    if ($html -ne $orig) {
        [System.IO.File]::WriteAllText($path, $html, [System.Text.UTF8Encoding]::new($false))
        Write-Host "Fixed: $path"
    }
}

# Event gallery folder — nav + assets
Get-ChildItem "$v3\event gallery\*.html" | ForEach-Object {
    Fix-File $_.FullName {
        param($h)
        $h = $h -replace '\\', '/'
        $h = $h -replace 'href="index\.html"', 'href="../index.html"'
        $h = $h -replace 'href="about-', 'href="../about/about-'
        $h = $h -replace 'href="media\.html"', 'href="../media.html"'
        $h = $h -replace 'href="contact\.html"', 'href="../contact.html"'
        $h = $h -replace 'href="faq\.html"', 'href="../faq.html"'
        $h = $h -replace 'href="news\.html"', 'href="../news/news.html"'
        $h = $h -replace 'href="news(\d+)\.html"', 'href="../news/news$1.html"'
        $h = $h -replace 'href="events\.html"', 'href="../upcoming events/events.html"'
        $h = $h -replace 'href="eto2026\.html"', 'href="../upcoming events/eto2026.html"'
        $h = $h -replace 'href="competitions\.html"', 'href="../programme/competitions.html"'
        $h = $h -replace 'href="certifications\.html"', 'href="../programme/certifications.html"'
        $h = $h -replace 'href="collaborations\.html"', 'href="../programme/collaborations.html"'
        $h = $h -replace 'href="projects\.html"', 'href="../programme/projects.html"'
        $h = $h -replace 'href="community\.html"', 'href="../programme/community.html"'
        $h = $h -replace 'href="membership\.html"', 'href="../programme/membership.html"'
        $h = $h -replace 'href="sponsors\.html"', 'href="../programme/sponsors.html"'
        $h = $h -replace 'href="scholarships\.html"', 'href="../programme/scholarships.html"'
        $h = $h -replace 'href="sisters\.html"', 'href="../programme/sisters.html"'
        $h = $h -replace 'href="\.\./competitions\.html"', 'href="../programme/competitions.html"'
        $h = $h -replace 'href="\.\./certifications\.html"', 'href="../programme/certifications.html"'
        $h = $h -replace 'href="\.\./collaborations\.html"', 'href="../programme/collaborations.html"'
        $h = $h -replace 'href="\.\./projects\.html"', 'href="../programme/projects.html"'
        $h = $h -replace 'href="\.\./community\.html"', 'href="../programme/community.html"'
        $h = $h -replace 'href="\.\./membership\.html"', 'href="../programme/membership.html"'
        $h = $h -replace 'href="\.\./sponsors\.html"', 'href="../programme/sponsors.html"'
        $h = $h -replace 'href="\.\./scholarships\.html"', 'href="../programme/scholarships.html"'
        $h = $h -replace 'href="\.\./sisters\.html"', 'href="../programme/sisters.html"'
        $h = $h -replace 'href="events\.html#past-events"', 'href="../about/about-history.html#archive"'
        $h = $h -replace 'href="about-history\.html"', 'href="../about/about-history.html"'
        $h = $h -replace 'src="kbi-hk\.js"', 'src="../kbi-hk.js"'
        $h = $h -replace 'href="kbi-hk\.css"', 'href="../kbi-hk.css"'
        return $h
    }
}

# about-history
Fix-File "$v3\about\about-history.html" {
    param($h)
    $h = $h -replace '\\', '/'
    $h = $h -replace 'href="index\.html"', 'href="../index.html"'
    $h = $h -replace 'href="events\.html"', 'href="../upcoming events/events.html"'
    $h = $h -replace 'href="news\.html"', 'href="../news/news.html"'
    $h = $h -replace 'href="media\.html"', 'href="../media.html"'
    $h = $h -replace 'href="contact\.html"', 'href="../contact.html"'
    $h = $h -replace 'href="faq\.html"', 'href="../faq.html"'
    $h = $h -replace 'href="event-gallery-', 'href="../event gallery/event-gallery-'
    $h = $h -replace 'src="images/', 'src="../event gallery/images/'
    return $h
}

# Root pages — about/ and events paths
@('contact.html','media.html','faq.html','index.html') | ForEach-Object {
    Fix-File "$v3\$_" {
        param($h)
        $h = $h -replace 'about\\', 'about/'
        $h = $h -replace 'href="about-who-we-are\.html"', 'href="about/about-who-we-are.html"'
        $h = $h -replace 'href="about-history\.html"', 'href="about/about-history.html"'
        $h = $h -replace 'href="about-impact\.html"', 'href="about/about-impact.html"'
        $h = $h -replace 'href="about-team\.html"', 'href="about/about-team.html"'
        $h = $h -replace 'href="events\.html"', 'href="upcoming events/events.html"'
        $h = $h -replace 'href="eto2026\.html"', 'href="upcoming events/eto2026.html"'
        $h = $h -replace 'href="news\.html"', 'href="news/news.html"'
        $h = $h -replace 'href="news(\d+)\.html"', 'href="news/news$1.html"'
        return $h
    }
}

# About folder — programme paths
Get-ChildItem "$v3\about\*.html" | ForEach-Object {
    Fix-File $_.FullName {
        param($h)
        $h = $h -replace 'href="competitions\.html"', 'href="../programme/competitions.html"'
        $h = $h -replace 'href="certifications\.html"', 'href="../programme/certifications.html"'
        $h = $h -replace 'href="collaborations\.html"', 'href="../programme/collaborations.html"'
        $h = $h -replace 'href="projects\.html"', 'href="../programme/projects.html"'
        $h = $h -replace 'href="community\.html"', 'href="../programme/community.html"'
        $h = $h -replace 'href="membership\.html"', 'href="../programme/membership.html"'
        $h = $h -replace 'href="sponsors\.html"', 'href="../programme/sponsors.html"'
        $h = $h -replace 'href="scholarships\.html"', 'href="../programme/scholarships.html"'
        $h = $h -replace 'href="sisters\.html"', 'href="../programme/sisters.html"'
        $h = $h -replace 'href="programmes\.html"', 'href="../programme/programmes.html"'
        $h = $h -replace 'href="index\.html"', 'href="../index.html"'
        $h = $h -replace 'href="events\.html"', 'href="../upcoming events/events.html"'
        $h = $h -replace 'href="eto2026\.html"', 'href="../upcoming events/eto2026.html"'
        $h = $h -replace 'href="news\.html"', 'href="../news/news.html"'
        $h = $h -replace 'href="media\.html"', 'href="../media.html"'
        $h = $h -replace 'href="contact\.html"', 'href="../contact.html"'
        $h = $h -replace 'href="faq\.html"', 'href="../faq.html"'
        return $h
    }
}

Write-Host 'Path fixes complete.'
