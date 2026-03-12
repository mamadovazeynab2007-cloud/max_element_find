1. Seçilmiş alqoritmin zaman mürəkkəbliyi nədir? O(n). Çünki massivdəki hər bir elementə yalnız bir dəfə baxılır.
2. Eyni problemi həll edən alternativ yanaşma varmı? Bəli, massivi sort() metodu ilə sıralayıb sonuncu elementi götürmək olar, lakin bu O(n log n) vaxt aparır və daha yavaşdır.
3. Niyə bu həll daha uyğundur? Çünki ən sürətli (xətti zaman) həlldir və əlavə yaddaş sahəsi tələb etmir.
