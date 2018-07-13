# 2018 Secim Twetleri ile İlgili Yapılabilecek İşlemler


Su an için herhangi bir data pre-processing işlemi yapmak veya networke ait bir çıkarım yapmak çok doğru olamayabilir, çünkü henüz networkun tam olarak yapısını bilmiyoruz. İleride ayni işlemleri tekrarlamak zorunda kalabiliriz ve yaptıklarımız boşa gidebilir.
O yüzden, benim önerim öncelikli olarak madde 3 ve daha sonra fırsat olursa madde 4 de belirtilen işlemleri yapmak. Bu daha mantıklı ve zaman kazandırıcı gibi duruyor. Madde 1 ve 2, data-pre-processing işlemlerini açıklıyor.
İlgili Maddeler
1- Oncelikle, tweetlerin unique olarak depolanmasi gerekiyor. Genellikle tek bir API anahtari ve sadece bir Streaming API baglantisi kullanılarak veri cekildiginde bu sorun oluşturmuyor. Ancak birden fazla baglanti varsa ayni tweet mükerrer olarak yer alabiliyor.

Bu sorunu çözmek için: toplanan her tweetin kendisine has bir “id” ve “id_str” değeri var bu değerler karşılaştırılabilir ve duplicate tweetler elenebilir.

2- Tweetlerin cinslerine göre ayrılması: Twitterde 3 tip network yapısı ilginç olabilir. Bunlar sırasıyla: “Retweet Network” ; “Mention Network” ; “Quoted Tweet Network”. Toplanan tweetlerin eninde sonunda bu üç farklı sınıfa ayrılması gerekiyor.
Not: “Quoted Tweetler” ayni zamanda “Quoted Retweet” de olabiliyor, o yüzden retweet networkunu oluştururken quoted tweetleri içine katmamak ve sadece “plain vanilla retweet” networkunu oluşturmak kafa karisikligini önlemek için mantıklı gözüküyor.

3- Konum tespiti. Ne tur bir çalışma yaparsak yapalım, konuma ait değerlendirmeler sunmak ilginç olacaktır. Su an, veriler parça parça gelirken, verilerdeki twitter kullanıcılarının profil bilgilerini ve konumlarını tespit etmek bize zaman kazandıracaktır.

Konum verisi daha önce konuştuğumuz gibi hem kullanıcın tweetinde hem profilinde yazıyor. Bu yüzden konum verisi tespiti için eğer varsa kullanıcının tweetlerindeki bilgi esas alınmalı, burada bilgi yoksa kullanıcının profilindeki bilgiler kullanılmalıdır. Bazıları profiline sadece ilce ya da semt ismi yazıyorlar, örneğin Kadıköy gibi. Çalışma kolaylığı için her 

konum Türkiye’deki bir şehirle eşleştirilmelidir.
Profil bilgisi REST API kullanılarak yada temel seviyede Webscraping (İlgili twitter sayfasını download edip, profili HTML kodları arasından ayrıştırmak) işlemiyle elde edilebilir.

Konum bilgisi tespit edilirken öncelik retweetlere verilmelidir. Hem retweet yapan hem de retweet yapılan kullanıcının konumu tespit edilmelidir. Yani her bir retweet, 2 adet kullanıcı içermektedir (retweet eden ve edilen) ve konum tespiti bu her iki kullanıcı için de yapılmalıdır.

4- Follower tespiti: Erdoğan Akşener Kılıçdaroğlu gibi belli başlı siyasi figürlerin twitterda pek çok takipçisi oluyor. Bu takipçi listesi milyonları bulduğu için ve Twitter API limitleri olduğu için bu listeyi indirmek zaman alıyor. Önemli siyasiler için follower listesi, yani onları takip (follow) eden Twitter kullanıcılarının listesini indirmeye şimdiden başlanabilir.
