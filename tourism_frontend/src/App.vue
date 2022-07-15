<script>
import { VueFinalModal } from 'vue-final-modal'
import 'vue3-carousel/dist/carousel.css';
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel';
import HelloWorldVue from "./components/Сarousel_items.vue";
import AppPhone from "./components/Carousel_itemsPhone.vue";
import $ from "jquery";
export default {
  name: 'CustomModal',
  inheritAttrs: false,
  emits: ['cancel'],

  data() {
    return{
      ring_of_altai: false,
      baikal: false,
      karelia: false,
      black_sea: false,
      kamchatka: false,
      siberia: false,
      shantar_islands: false,
      blue_and_lena_rivers: false,
      yamal_and_ural: false,
      elbrus: false,
      name: "",
      phone_number: "",
      email: "",
      comment: "",
      check: false,
    }
  },
  methods: {
    hideModal() {
      this.open = false;
    },
    saveName(event){
      this.name = event.target.value;
    },
    savePhone(event){
      this.phone_number= event.target.value;
    },
    saveEmail(event){
      this.email = event.target.value;
    },
    saveComment(event){
      this.comment = event.target.value;
    },
    saveBooking() {
      $.ajax({
        url: "http://127.0.0.1:8000/api/v1/application/",
        type: "POST",
        data: {
          name: this.name,
          phone: this.phone_number,
          email: this.email,
          comment: this.comment
        },
        success: (response) => {
          alert(response.data)
        },
        error: (data) => {
          alert(data.responseJSON.error)
        }
      })
    },
  },
  components: {
    carouselImg: HelloWorldVue,
    carouselImgPhone: AppPhone,
    VueFinalModal,
    Carousel,
    Slide,
    Pagination,
    Navigation,
  }
}



</script>
<template>
  <!DOCTYPE html>
  <html lang="ru">
  <head>
    <meta charset="UTF-8">
    <title>Russian Touristik</title>
    <link rel="stylesheet" type="text/css" href="assets/1style.css">
    <link rel="stylesheet" type="text/css" href="assets/magnific-popup.css">
  </head>
  <body>
  <header class="header">
    <div class="container">
      <div class="header__inner">
        <div class="header__top">
          <a class="logo">
            <img class="logo" src="./assets/images/logo.png"  alt="" href="#">
          </a>
          <div class="header__phone">

            <a class="header__phone-number" href="tel:88005553535" >
              <b>тел. 8-800-555-35-35 </b>
            </a>
          </div>
          <nav class="menu">
            <ul class="menu__list">
              <li class="menu__item"> <a class="menu__link" href="#booking">  <b>Бронирование</b>  </a></li>
              <li class="menu__item"> <a class="menu__link" href="#popular_tours">  <b>Популярные предложения</b> </a></li>
              <li class="menu__item"> <a class="menu__link" href="#main_tours">  <b>Наши услуги</b> </a></li>
              <li class="menu__item"> <a class="menu__link" href="#photo_gallery">  <b>Фотогалерея</b> </a></li>
              <li class="menu__item"> <a class="menu__link" href="#about">  <b>О турах</b> </a></li>
            </ul>
          </nav>
        </div>
        <h1 class="header__title">Путешествуй по России</h1>

        <br><br>

        <div class="header__content">
          <p class="header__descr">Туры по самомым живописным, необычным местам.
            Отвлекись от городской суеты и насладись прекрасными видами своей Родины!</p>

          <a class="header__btn" href="#booking"><b>Оставить заявку</b> </a>

          <div class="header__arrow">
            <a class="header__arrow-link" href="#directions"><img class="header__arrow-img" src="./assets/images/arrow.svg" alt=""></a>
          </div>
        </div>
      </div>
    </div>
  </header>

  <div id="directions" class="direction">
    <div class="container">
      <div class="direction__inner">
        <div class="direction__item">
          <img src="./assets/images/bajkal.jpg" alt="" class="direction__img">
          <p class="description__text">Байкал</p>
        </div>
        <div class="direction__item">
          <img src="./assets/images/osetiya.jpg" alt="" class="direction__img">
          <p class="description__text">Осетия</p>
        </div>
        <div class="direction__item">
          <img src="./assets/images/rosehuter.jpg" alt="" class="direction__img">
          <p class="description__text">Роза Хутор</p>
        </div>
        <div class="direction__item">
          <img src="./assets/images/sheregesh.jpg" alt="" class="direction__img">
          <p class="description__text">Шерегеш</p>
        </div>
        <div class="direction__item">
          <img src="./assets/images/altai.jpg" alt="" class="direction__img">
          <p class="description__text">Алтай</p>
        </div>
        <div class="direction__item">
          <img src="./assets/images/kamchatka.jpg" alt="" class="direction__img">
          <p class="description__text">Камчатка</p>
        </div>
        <div class="direction__item">
          <img src="./assets/images/vladivostok.jpg" alt="" class="direction__img">
          <p class="description__text">Владивосток</p>
        </div>
        <div class="direction__item">
          <img src="./assets/images/ural.jpg" alt="" class="direction__img">
          <p class="description__text">Урал</p>
        </div>
        <div class="direction__item">
          <img src="./assets/images/yamal.jpg" alt="" class="direction__img">
          <p class="description__text">Ямал</p>
        </div>
        <div class="direction__item">
          <img src="./assets/images/kareliya.jpg" alt="" class="direction__img">
          <p class="description__text">Карелия</p>
        </div>
        <div class="direction__item">
          <img src="./assets/images/kislovodsk.jpg" alt="" class="direction__img">
          <p class="description__text">Кисловодск</p>
        </div>
        <div class="direction__item">
          <img src="./assets/images/privoljie.jpg" alt="" class="direction__img">
          <p class="description__text">Приволжье</p>
        </div>
      </div>
    </div>
  </div>

  <section id="main_tours" class="travel-info">
    <div class="container">
      <h2 class="travel-info__title title">Наши услуги</h2>
      <div class="travel-info__items">
        <div class="travel-info__item">
          <img src="./assets/images/icon-1.svg" alt="" class="travel-info__img">
          <p class="travel-info__text">Полная организация отдыха: групповые и индивидуальные туры.</p>
        </div>

        <div class="travel-info__item">
          <img src="./assets/images/icon-2.svg" alt="" class="travel-info__img">
          <p class="travel-info__text">Организация трансфера из любой точки страны</p>
        </div>

        <div class="travel-info__item">
          <img src="./assets/images/icon-3.svg" alt="" class="travel-info__img">
          <p class="travel-info__text">Проживание в отелях по маршруту</p>
        </div>

        <div class="travel-info__item">
          <img src="./assets/images/icon-4.svg" alt="" class="travel-info__img">
          <p class="travel-info__text">Аренда автомобилей и любого вида транспорта</p>
        </div>

        <div class="travel-info__item">
          <img src="./assets/images/icon-5.svg" alt="" class="travel-info__img">
          <p class="travel-info__text">Медицинская страховка</p>
        </div>

        <div class="travel-info__item">
          <img src="./assets/images/icon-6.svg" alt="" class="travel-info__img">
          <p class="travel-info__text">Сопровождение гидов</p>
        </div>

        <div class="travel-info__item">
          <img src="./assets/images/icon-7.svg" alt="" class="travel-info__img">
          <p class="travel-info__text">Организация VIP-туров</p>
        </div>

      </div>
    </div>
  </section>

  <section class="test">
    <div class="container">
      <h2 id="popular_tours" class="popular__title title"><b>Популярные предложения</b></h2>
      <div class="biggrid">
        <div class="smallgrid">
          <a id="ring_of_altai" href="#ring_of_altai"><img class="popular__box" src="./assets/images/popf.jpg" @click="ring_of_altai = true" alt="" ></a>
          <a id="baikal" href="#baikal"><img class="popular__box" src="./assets/images/pops.jpg" @click="baikal = true" alt="" ></a>
          <a id="karelia" href="#karelia"><img class="popular__box" src="./assets/images/popfour.jpg" @click="karelia = true" alt="" ></a>
          <a id="black_sea" href="#black_sea"><img class="popular__box" src="./assets/images/popsix.jpg" @click="black_sea = true" alt="" ></a>
        </div>
        <a id="kamchatka" href="#kamchatka"><img class="popular__boxe" src="./assets/images/popt.jpg" @click="kamchatka = true" alt="" ></a>
        <a id="siberia" href="#siberia"><img class="popular__boxe" src="./assets/images/popfive.jpg" @click="siberia = true" alt="" ></a>
        <div class="smallgrid">
          <a id="shantar_islands" href="#shantar_islands"><img class="popular__box" src="./assets/images/popseven.jpg" @click="shantar_islands = true" alt="" ></a>
          <a id="blue_and_lena_rivers" href="#blue_and_lena_rivers"><img class="popular__box" src="./assets/images/popeight.jpg" @click="blue_and_lena_rivers = true" alt="" ></a>
          <a id="yamal_and_ural" href="#yamal_and_ural"><img class="popular__box" src="./assets/images/popnine.jpg" @click="yamal_and_ural = true" alt="" ></a>
          <a id="elbrus" href="#elbrus"><img class="popular__box" src="./assets/images/popten.jpg" @click="elbrus = true" alt="" ></a>
        </div>
      </div>
      <div class="modal__action">
      </div>
      <a href="#booking">
        <img src="./assets/images/btn-order.png" alt="" class="zakaz">
      </a>
    </div>
  </section>


  <div>
    <vue-final-modal id="ring_of_altai" v-model="ring_of_altai" classes="modal-container" content-class="modal-content">
      <span class="modal__title">Золотое кольцо Алтая</span>
      <div class="modal__content">
          <img src="./assets/images/fpop.jpg" class="modal__img" alt="" >
          <p class="description__text">Мы приглашаем вас в люкспедицию премиум-класса по вдохновляющим местам Алтайских гор – вас ждет роуд-трип по самой впечатляющей дороге России и объекты Всемирного наследия ЮНЕСКО: снежные вершины и ледники, высокогорные озера и водопады, памятники древних цивилизаций и встреча с коренным населением.
          Готовы отправиться в Вип-тур по Алтаю вместе с нами, чтобы получить тотальную перезагрузку в единении с природой, найти единомышленников и будущих друзей, очистить душу и вернуться новым человеком?</p>
          <div class="modal__action">
            <v-button class="modal__close" @click="ring_of_altai = false"><img src="./assets/images/krest.png" alt="" class="krest"></v-button>
          </div>
      </div>
    </vue-final-modal>

    <vue-final-modal id="baikal" v-model="baikal" classes="modal-container" content-class="modal-content">
      <span class="modal__title">Байкал</span>
      <div class="modal__content">
          <img src="./assets/images/spop.jpg" class="modal__img" alt="" >
          <p class="description__text">Вас ждет невероятно насыщенное и разнообразное приключение! Круиз на яхте, джиппинг-программа по Мамаю и Тажеранским степям, невероятная SPA-программа, ваш персональный бассейн под открытым небом, и десятки незабываемых мест Байкала с его неповторимой красотой и энергетикой! Все в этом туре создано для
          получения незабываемых эмоций от Байкала с высоким уровнем комфорта.</p>
          <div class="modal__action">
            <v-button class="modal__close" @click="baikal = false"><img src="./assets/images/krest.png" alt="" class="krest"></v-button>
          </div>
      </div>
    </vue-final-modal>

    <vue-final-modal id="karelia" v-model="karelia" classes="modal-container" content-class="modal-content">
      <span class="modal__title">Карелия</span>
      <div class="modal__content">
          <img src="./assets/images/fourpop.jpg" class="modal__img" alt="" >
          <p class="description__text">Приглашаем вас насладиться неповторимым отдыхом в Северном Приладожье, одном из самых живописных районов Карелии. Подарите себе возможность окунуться в дикую природу и при этом жить в лагере со всеми удобствами.
          Добро пожаловать в глэмпинг, полевой лагерь с несравненным уровнем комфорта. Уютные шатры–сферы на несколько дней станут Вашим домом, а дружеские посиделки после активного дня в купольном шатре с панорамным видом на Ладожское озеро, несомненно, подарят вам незабываемые впечатления!
            Откройте для себя 5 дней настоящих приключений. Здесь вас ждут скалистые острова и заповедные бухты Ладожских шхер, шумные пороги реки Янис, старинные карельские деревни и знаменитый Валаамский архипелаг.</p>
          <div class="modal__action">
            <v-button class="modal__close" @click="karelia = false"><img src="./assets/images/krest.png" alt="" class="krest"></v-button>
          </div>
      </div>
    </vue-final-modal>

    <vue-final-modal id="black_sea" v-model="black_sea" classes="modal-container" content-class="modal-content">
      <span class="modal__title">Чёрное море</span>
      <div class="modal__content">
          <img src="./assets/images/sixpop.jpg" class="modal__img" alt="" >
          <p class="description__text">Специально для вас наша команда разработала уникальный маршрут по Крымскому полуострову. Вы сможете посетить удивительные места, будете путешествовать по горам, купаться в море, исследовать древние города и наслаждаться великолепной природой.
          Вы будете путешествовать на джипах, пешком, на катерах. Полакомитесь морскими деликатесами, окунётесь в открытое море, исследуете подземный мир множества пещер, познакомитесь с самым мистическим местом Крыма, узнаете легенды и предания этого великолепного места, окунётесь в историю этого уголка нашей страны.</p>
          <div class="modal__action">
            <v-button class="modal__close" @click="black_sea = false"><img src="./assets/images/krest.png" alt="" class="krest"></v-button>
          </div>
      </div>
    </vue-final-modal>

    <vue-final-modal id="kamchatka" v-model="kamchatka" classes="modal-container" content-class="modal-content">
      <span class="modal__title">Камчатка</span>
      <div class="modal__content">
          <img src="./assets/images/tpop.jpg" class="modal__img" alt="" >
          <p class="description__text">Существует поверье, что Драконы, в древности существовавшие на нашей планете, обиделись на людей за изобретение спичек и улетели на Камчатку. Вырыли в долине норы, и живут там по сей день, грустно выпуская пар на поверхность. Никогда не знаешь, какие чудеса поджидают вас в долине Гейзеров. Вдруг вы встретите там старого доброго Горыныча.
          А если серьёзно, то каждый человек хоть раз в жизни должен посетить это уникальное место. На небольшой территории соседствует множество уникальных природных явлений, некоторые из них не встречаются больше нигде в мире. Например, новый минерал, который образуется на наших глазах, или самые древние микроорганизмы планеты.
          Самое захватывающее то, что увидеть действующие вулканы, живописные виды и ярко-бирюзовое озеро вы сможете как на ладони из иллюминатора вертолёта. Прекрасный пейзаж перед глазами, океан воздуха под ногами и состояние полёта как во сне. Вот, что ждёт вас в этом путешествии.
          Обед в Налычевской долине и купание в целебных термальных источниках станут идеальным завершением дня.
          </p>
          <div class="modal__action">
            <v-button class="modal__close" @click="kamchatka = false"><img src="./assets/images/krest.png" alt="" class="krest"></v-button>
          </div>
      </div>
    </vue-final-modal>

    <vue-final-modal id="siberia" v-model="siberia" classes="modal-container" content-class="modal-content">
      <span class="modal__title">Шумак</span>
      <div class="modal__content">
          <img src="./assets/images/fivepop.jpg" class="modal__imge" alt="" >
          <p class="description__text">Увлекательный перелет на вертолете, во время которого мы насладимся потрясающими видами долин рек Иркут, Китой, Шумак и Тункинской долины, знаменитой своими альпийскими лугами;  Трекинг к водопаду Мраморный, путь к которому проходит по кедровой тайге; Прогулка к столбам Хуухэйн-Хада , где обитает дух — хранитель Шумака; Экскурсия к Шумакским минеральным источникам, во время которой можно будет не только попробовать воду из источников, но и принять минеральную ванну под открытым небом; Пешие путешествия к Золотым и Изумрудным озерам, по пути к которым нам обязательно встретятся красивейшие водопады и горные ручейки; Для любителей йоги ежедневные утренние занятия, дающие заряд бодрости на весь день.
          </p>
          <div class="modal__action">
            <v-button class="modal__close" @click="siberia = false"><img src="./assets/images/krest.png" alt="" class="krest"></v-button>
          </div>
      </div>
    </vue-final-modal>

    <vue-final-modal id="shantar_islands" v-model="shantar_islands" classes="modal-container" content-class="modal-content">
      <span class="modal__title">Шантарские острова</span>
      <div class="modal__content">
          <img src="./assets/images/sevenpop.jpg" class="modal__img" alt="" >
          <p class="description__text">Тур на Шантарский архипелаг - это невероятное и удивительное приключение в одно из самых малоисследованных и малоизученных диких мест на планете Земля. Из-за своей труднодоступности Шантарский архипелаг смог сохранить свою первозданную красоту, и перед вами откроется удивительный мир дикой природы во всем своем первозданном великолепии.
          Только здесь вы сможете понаблюдать за гренландскими китами, косатками, поплавать рядом с ними в их естественной среде
          обитания так близко, что невольно возникает желание прикоснуться к ним . А дальневосточные нерпы будут везде и всюду вас сопровождать на протяжении всего тура по архипелагу. Из-за этого сложится впечатление, что это не вы, а они наблюдают за вами.
          </p>
          <div class="modal__action">
            <v-button class="modal__close" @click="shantar_islands = false"><img src="./assets/images/krest.png" alt="" class="krest"></v-button>
          </div>
      </div>
    </vue-final-modal>

    <vue-final-modal id="blue_and_lena_rivers" v-model="blue_and_lena_rivers" classes="modal-container" content-class="modal-content">
      <span class="modal__title">Якутия</span>
      <div class="modal__content">
          <img src="./assets/images/goldenrockspop.jpg" class="modal__img" alt="" >
          <p class="description__text">Вас ждет сплав по рекам Лена и Синяя, во время которого вы посетите главную природную достопримечательность Якутии — Ленские столбы. Эти вертикальные скалы, вытянувшиеся на много километров вдоль берегов, являются объектами Всемирного наследия ЮНЕСКО. Их формы неповторимы и вызывают интересную игру воображения: одни видят в них молчаливых каменных воинов, другие — причудливые по форме замки, кому-то они напоминают животных или птиц.</p>
          <div class="modal__action">
            <v-button class="modal__close" @click="blue_and_lena_rivers = false"><img src="./assets/images/krest.png" alt="" class="krest"></v-button>
          </div>
      </div>
    </vue-final-modal>

    <vue-final-modal id="yamal_and_ural" v-model="yamal_and_ural" classes="modal-container" content-class="modal-content">
      <span class="modal__title">Ямал и Полярный Урал</span>
      <div class="modal__content">
          <img src="./assets/images/yamalpop.jpg" class="modal__img" alt="" >
          <p class="description__text">Глубоко в ямальской тундре, в окружении остропиких вершин укрылись озера Хадатаёганлор — одни из самых живописных на Полярном Урале. В их водах водится множество рыбы, а неподалеку устраивают стоянки ханты-оленеводы. Невероятные пейзажи, знакомство с бытом кочевников и локации, где почти не бывает туристов — вот что ждет вас в этой экспедиции.
          В этой экспедиции вы проведете неделю на берегу озера Хадатаёганлор, на квадроциклах-вездеходах исследуете территорию природного Полярно-Уральского парка и познакомитесь с семьей кочующих оленеводов.</p>
          <div class="modal__action">
            <v-button class="modal__close" @click="yamal_and_ural = false"><img src="./assets/images/krest.png" alt="" class="krest"></v-button>
          </div>
      </div>
    </vue-final-modal>

    <vue-final-modal id="elbrus" v-model="elbrus" classes="modal-container" content-class="modal-content">
      <span class="modal__title">Эльбрус</span>
      <div class="modal__content">
          <img src="./assets/images/tenpop.jpg" class="modal__img" alt="" >
          <p class="description__text">Эта программа - отличный выбор, если вы хотите маршрут полегче, но все же хотели бы пройти весь путь своими ногами - без канатки, с рюкзаком и палаткой. Само восхождение на вершину проходит по самому популярному южному маршруту. Но подход к верхнему лагерю лежит в стороне от отелей и канатки. Таким образом, маршрут сочетает в себе относительную простоту и в то же время близость к природе. Подходит для первого раза, если у вас есть хотя бы обычная средняя физ. форма. Цена этого маршрута самая низкая среди всех наших программ.</p>
          <div class="modal__action">
            <v-button class="modal__close" @click="elbrus = false"><img src="./assets/images/krest.png" alt="" class="krest"></v-button>
          </div>
      </div>
    </vue-final-modal>
  </div>


  <section class="map">
    <div class="container">
      <h2 class="map__title title"><b>Карта России</b></h2>
      <div class="map__responsive">
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d37494223.23909492!2d103!3d55!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x453c569a896724fb%3A0x1409fdf86611f613!2z0KDQvtGB0YHQuNGP!5e0!3m2!1sru!2sru!4v1657022899867!5m2!1sru!2sru" class="map-box"   allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
    </div>
  </section>

  <section class="about" id="about">
    <div class="container">
      <div class="about__inner">
        <div class="about__content">
          <h2 class="about__title title"><b>О российском туризме</b></h2>
          <p class="about__text">Россия богата экскурсионными маршрутами и объектами: белокаменная Москва,
            Санкт–Петербург – город музей, многоликая Карелия, памятники древнерусских городов Золотого кольца,
            необъятный Байкал, вулканы Камчатки… Москва является самым посещаемым туристами местом в России.
            Величие Кремля, Красная площадь, Собор Василия Блаженного, Поклонная гора, незабываемые прогулки
            по Москве наполнят туристов русским духом, а посещение известных во всем мире музеев и галерей
            подарят непременно массу ярких впечатлений.<br><br>Большинство природных регионов России имеют
            труднодоступные памятники археологии и культуры, которые представляют несомненный интерес для туристов.
            Для каждого человека слово «приключение» имеет свой глубокий смысл. Для одних это путешествие в Долину
            Гейзеров на Камчатке, лыжный тур на Южный Урал или сафари на собачьих упряжках в Карелии, для других – это
            рафтинг на Алтае, конные маршруты по Кавказу или джип-туры, для третьих - рыболовные туры в Астрахани или
            поиск сокровищ на Финском заливе.
            Любители приключений могут выбрать любой вариант необычного отдыха: от традиционной прогулки на яхте до
            захватывающих дух полетов на сверхзвуковом самолете.
          </p>
        </div>
        <div class="about__popup">
          <a href="https://www.youtube.com/watch?v=lyh2kAjcmSY" target="_blank" class="popup__link">
            <img src="./assets/images/popup.svg" alt="" class="about__link-img">
          </a>
        </div>
      </div>
    </div>
  </section>


  <section class="carus" id="photo_gallery">
    <div class="container-carousel">
      <h2 class="carousel__title title"><b>Фотогалерея</b></h2>
      <div><carouselImg/></div>
    </div>

    <div class="container-carouselph">
      <h2 class="carousel__title title"><b>Фотогалерея</b></h2>
      <div><carouselImgPhone/></div>
    </div>
  </section>



  <section class="tour">
    <div class="container">
      <h2 class="tour__title title"><b>ТУРЫ ПО РОССИИ ПРЕМИУМ КЛАССА</b></h2>
      <div class="tour__box">

        <p class="tour__text">VIP туры - это уникальное знакомство с многогранной
          Россией, наблюдение за дикими животными в их привычной среде обитания, возможность побывать в местах, где еще не ступала нога обычного человека.
        </p>

        <p class="tour__text"><span>«Турист»</span> специализируется на элитном туризме и представляет своим
          клиентам
          уникальные программы VIP туров. Среди представленных вариантов можно найти нечто неповторимое, по вашему
          вкусу.
        </p>

        <p class="tour__text">Если вы желаете отправиться в самое незабываемое путешествие в вашей жизни, побывать в
          уникальных местах и увидеть то, что удается лицезреть немногим, тогда VIP туры созданы для вас.</p>

        <p class="tour__text">Данные туры выбирают туристы, которые предпочитают динамичный, яркий, насыщенный эмоциями
          и впечатлениями отдых.
          Программы премиум туров по России рассчитаны на определенную группу людей, которые под покровительством
          куратора, осуществляют увлекательное путешествие по заранее спланированному маршруту. Мы ориентированы на
          клиентов ELITE класса, поэтому все предложения, представленные в нашей коллекции, отличаются высшим классом,
          детально продуманной программой, первоклассным сервисом и индивидуальным подходом к каждому участнику
          путешествия. У нас на сайте вы можете прочитать все подробности о программах уже сформированных туров по
          России.</p>

      </div>
      <div class="tour__info">
        <div class="tour__info-item">
          10
          <p class="tour__info-text">
            лет успешной
            работы
          </p>
        </div>

        <div class="tour__info-item">
          26
          <p class="tour__info-text">
            гостиниц без
            посредников
          </p>
        </div>

        <div class="tour__info-item">
          30+
          <p class="tour__info-text">
            собственных
            туров
          </p>
        </div>

        <div class="tour__info-item">
          5477000
          <p class="tour__info-text">
            кв. км – площадь наших
            путешествий
          </p>
        </div>

        <div class="tour__info-item">
          15600
          <p class="tour__info-text">
            довольных туристов
          </p>
        </div>

      </div>
    </div>
  </section>

  <section id="booking" class="booking">
    <div class="container">
      <h2 class="booking__title title"><b>Забронируйте отдых в России</b></h2>
      <form class="booking__form">
        <input type="text" class="booking__input" placeholder="Ваше имя" @input="saveName">
        <input type="text" class="booking__input" placeholder="Телефон вида 7xxx..." @input="savePhone">
        <input type="text" class="booking__input" @keyup.enter="saveBooking" placeholder="E-mail" @input="saveEmail">
        <textarea class="booking__area" placeholder="Комментарий" @input="saveComment"></textarea>
        <button :disabled="!check" class="booking__btn" id="submitButton" type="submit" v-on:click.prevent="saveBooking">Отправить заявку</button>
        <label class="booking__label">
          <input type="checkbox" class="booking__checkbox" v-model="check" required="required">
          <span class="booking__checkbox-style"></span>
          <a class="booking__argument" target="_blank" href="https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwid56ixnO74AhXdYPEDHWDDDlIQFnoECAQQAQ&url=https%3A%2F%2Fnetrack.ru%2Fstorage%2F2019%2F12%2FPrilozhenie-N2.-Forma-soglasiya-na-obrabotku-personalnykh-dannykh.pdf&usg=AOvVaw0B18DU1FPRAgjprlC5hZur">Согласие на обработку персональных данных</a>
        </label>
      </form>
    </div>
  </section>

  <footer class="footer">
    <div class="container">
      <div class="footer__box">

        <div class="footer__info">
          <p class="footer__box-title">Турагентство «Турист»</p>
          <p class="footer__copy">© 2022. Все права защищены</p>
          <a target="_blank" href="https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi0v7LWoO74AhUKXfEDHe7yAj4QFnoECAQQAQ&url=https%3A%2F%2Fxn--80ajghhoc2aj1c8b.xn--p1ai%2Fupload%2Fconf_ru.pdf&usg=AOvVaw2myvfueRBz2lpReQGJ0kel" class="footer__link">Политика конфиденциальности</a>
        </div>

        <div class="footer__address">
          <p class="footer__box-title">Адрес:</p>
          <p class="footer__address-text">г. Москва, Гороховский переулок, 4 ст 4,
            общежитие «Дом Студента», 14 этаж</p>
        </div>

        <div class="footer__contacts">
          <p class="footer__box-title">Заказ туров и бронирование:</p>
          <a href="tel:80508543543" class="footer__phone">тел. 8-800-555-35-35</a>
          <a href="mailto:safari_turistic@gmail.com" class="footer__mail"> e-mail: apartment145a@gmail.com</a>
        </div>

      </div>
    </div>
  </footer>


  </body>
  </html>
</template>

<style>
@import 'assets/1style.css';
@import 'assets/magnific-popup.css';

</style>
<style scoped>
::v-deep(.modal-container) {
  display: flex;
  justify-content: center;
  align-items: center;
}
::v-deep(.modal-content) {
  position: relative;
  display: flex;
  flex-direction: column;
  max-height: 90%;
  margin: 20px;
  padding: 10px;
  border: 1px solid #e2e8f0;
  border-radius: 0.25rem;
  background: #fff;
}

</style>

<style scoped>
.dark-mode div ::v-deep(.modal-content) {
  border-color: #2d3748;
  background-color: #1a202c;
}
</style>

<style>
  @media (max-width: 391px) {
    ::v-deep(.modal-content) {
      max-height: 90%;
      width: 270px;
    }
  }
</style>

