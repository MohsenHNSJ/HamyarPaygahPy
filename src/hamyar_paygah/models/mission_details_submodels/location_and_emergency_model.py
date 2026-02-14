"""Location and emergency sub-model for Mission details model."""
# pylint: disable=R0902

from dataclasses import dataclass
from enum import Enum


class LocationType(Enum):
    """Types of emergency location."""

    # Buildings
    RESIDENTIAL = "Maskooni"
    """Residential buildings such as houses, apartments, or private dwellings."""
    INDUSTRIAL = "Sanati"
    """Industrial facilities such as factories, plants, or workshops."""
    SPORTS = "Varzeshi"
    """Sports facilities including stadiums, gyms, or sports complexes."""
    EDUCATIONAL = "Amoozeshi"
    """Educational institutions such as schools, universities, or training centers."""
    MEDICAL = "Darmani"
    """Medical facilities including hospitals, clinics, or health centers."""
    OFFICE = "Edari"
    """Administrative or office buildings, including government or corporate offices."""

    # Roads
    HIGHWAY = "AzadRah"
    """Highways designed for high-speed, long-distance traffic."""
    EXPRESSWAY = "BozorgRah"
    """Major express roads with heavy traffic and limited access points."""
    MAIN_ROAD = "RahAsli"
    """Primary roads connecting major urban or regional areas."""
    SECONDARY_ROAD = "RahFari"
    """Secondary or feeder roads branching from main roads."""
    RURAL_ROAD = "RahRoostaei"
    """Rural roads serving villages or low-traffic countryside areas."""

    @property
    def persian_label(self) -> str:
        """Returns the persian label of the set location type."""
        return {
            LocationType.RESIDENTIAL: "مسکونی",
            LocationType.INDUSTRIAL: "صنعتی",
            LocationType.SPORTS: "ورزشی",
            LocationType.EDUCATIONAL: "آموزشی",
            LocationType.MEDICAL: "درمانی",
            LocationType.OFFICE: "اداری",
            LocationType.HIGHWAY: "آزادراه",
            LocationType.EXPRESSWAY: "بزرگراه",
            LocationType.MAIN_ROAD: "راه اصلی",
            LocationType.SECONDARY_ROAD: "راه فرعی",
            LocationType.RURAL_ROAD: "راه روستایی",
        }[self]


class AccidentType(Enum):
    """Types of accidents or injury mechanisms involved in an emergency mission."""

    SUICIDE = "KhodKoshi"
    """Intentional self-harm or suicide attempt."""
    DROWNING = "GharghShodegi"
    """Drowning or near-drowning incident."""
    HEAT_STROKE = "GarmaZadegi"
    """Heat-related illness such as heat exhaustion or heat stroke."""
    AIRWAY_OBSTRUCTION = "EnsedadRaheHavaei"
    """Airway obstruction leading to breathing difficulty or suffocation."""
    ELECTRIC_SHOCK = "barghGereftegi"
    """Electrical shock caused by current passing through the body."""
    ANIMAL_BITE = "HeivanGazidegi"
    """Injury caused by animal bite or attack."""
    VIOLENCE = "Khoshoonat"
    """Injury related to physical violence or assault."""
    COMMON_COLD = "SarmaKhordegi"
    """Cold-related injury"""
    INSECT_BITE = "GazesheHashare"
    """Insect bite or sting."""
    HOT_OBJECT_BURN = "JesmeDagh"
    """Burn caused by contact with a hot solid object."""
    CHEMICAL_EXPOSURE = "Shimiaei"
    """Chemical exposure or chemical burn."""
    HOT_LIQUID_BURN = "MayeatDagh"
    """Burn caused by hot liquids or scalding."""
    ELECTRICAL_BURN = "Electric"
    """Burn injury caused by electrical energy without systemic shock."""
    FIRE = "Harigh"
    """Fire-related injury including flame burns or smoke exposure."""
    OTHER_CAUSES = "ElalHavadesSayer"
    """Other or unspecified causes of accidents or injuries."""
    CARBON_MONOXIDE_POISONING = "CO"
    """Carbon monoxide poisoning."""
    DRUG_OVERDOSE = "Daroo"
    """Drug or medication overdose or poisoning."""
    NARCOTIC_POISONING = "MavadMokhader"
    """Intoxication or poisoning caused by narcotics or illicit substances."""
    TOXIC_POISONING = "Sommom"
    """Poisoning caused by toxic substances other than drugs or narcotics."""
    ALCOHOL_INTOXICATION = "Alekol"
    """Alcohol intoxication or poisoning."""
    SAME_LEVEL_FALL = "Hamtaraz"
    """Fall occurring on the same surface level, such as slipping or tripping."""
    DIFFERENT_LEVEL_FALL = "GheireHamtaraz"
    """Fall from a different level, such as from a height or between floors."""
    MECHANICAL_IMPACT = "BarkhordBanirooMechanic"
    """Injury caused by impact or collision involving mechanical force."""
    FROSTBITE_TRAUMA = "TromaYakhBandan"
    """Cold-induced traumatic injury caused by freezing of body tissues (frostbite)."""

    @property
    def persian_label(self) -> str:
        """Persian label of the set accident type."""
        return {
            AccidentType.SUICIDE: "خودکشی",
            AccidentType.DROWNING: "غرق‌شدگی",
            AccidentType.HEAT_STROKE: "گرمازدگی",
            AccidentType.AIRWAY_OBSTRUCTION: "انسداد راه هوایی",
            AccidentType.ELECTRIC_SHOCK: "برق‌گرفتگی",
            AccidentType.ANIMAL_BITE: "حیوان‌گزیدگی",
            AccidentType.VIOLENCE: "خشونت",
            AccidentType.COMMON_COLD: "سرماخوردگی",
            AccidentType.INSECT_BITE: "گزش حشره",
            AccidentType.HOT_OBJECT_BURN: "سوختگی با جسم داغ",
            AccidentType.CHEMICAL_EXPOSURE: "مسمومیت یا سوختگی شیمیایی",
            AccidentType.HOT_LIQUID_BURN: "سوختگی با مایع داغ",
            AccidentType.ELECTRICAL_BURN: "سوختگی الکتریکی",
            AccidentType.FIRE: "حریق",
            AccidentType.OTHER_CAUSES: "سایر علل حوادث",
            AccidentType.CARBON_MONOXIDE_POISONING: "مسمومیت با مونوکسید کربن",
            AccidentType.DRUG_OVERDOSE: "اوردوز دارویی",
            AccidentType.NARCOTIC_POISONING: "مسمومیت با مواد مخدر",
            AccidentType.TOXIC_POISONING: "مسمومیت با مواد سمی",
            AccidentType.ALCOHOL_INTOXICATION: "مسمومیت الکلی",
            AccidentType.SAME_LEVEL_FALL: "سقوط هم‌سطح",
            AccidentType.DIFFERENT_LEVEL_FALL: "سقوط از ارتفاع",
            AccidentType.MECHANICAL_IMPACT: "برخورد مکانیکی",
            AccidentType.FROSTBITE_TRAUMA: "ترومای یخ‌زدگی",
        }[self]


class IllnessType(Enum):
    """Primary medical conditions or symptoms reported during an emergency mission."""

    CARDIAC = "Ghalbi"
    """Cardiac-related condition such as chest pain, arrhythmia, or heart failure."""
    RESPIRATORY = "Tanafosi"
    """Respiratory distress or breathing-related condition."""
    WEAKNESS_FATIGUE = "Zaf_Bihali"
    """General weakness, fatigue, or lethargy without a specific diagnosis."""
    STROKE = "SakteMaghzi"
    """Cerebrovascular accident (stroke) or acute neurological deficit."""
    PSYCHIATRIC_DISORDER = "EkhtelalRavani"
    """Psychiatric or mental health disorder requiring emergency evaluation."""
    FEVER_SEIZURE = "TabTashanoj"
    """Seizure associated with fever, commonly febrile convulsion."""
    HYPERTENSION = "AfzayeshFesharKoon"
    """Elevated blood pressure or hypertensive crisis."""
    HYPOGLYCEMIA = "Haipogelesimi"
    """Low blood glucose level causing neurological or systemic symptoms."""
    HYPERGLYCEMIA = "Hipergelesimi"
    """High blood glucose level, possibly diabetic emergency."""
    DECREASED_CONSCIOUSNESS = "KaheshHooshyari"
    """Reduced level of consciousness, drowsiness, or altered mental status."""
    PHYSICAL_ASSAULT = "ZarbJarh"
    """Injury resulting from physical fighting or assault between individuals."""
    HYSTERIA = "Histerik"
    """Acute hysterical or psychosomatic reaction presenting as an emergency."""
    ABDOMINAL_PAIN = "DardShekami"
    """Acute abdominal pain of unknown or known origin."""
    RENAL_COLIC = "RenalKoolik"
    """Severe flank pain typically caused by kidney stones."""
    CHILDBIRTH = "Zayeman"
    """Active labor or complications related to childbirth."""
    MISCARRIAGE = "Seght"
    """Pregnancy loss or complications related to miscarriage."""

    @property
    def persian_label(self) -> str:
        """Persian label of the set illness type."""
        return {
            IllnessType.CARDIAC: "مشکل قلبی",
            IllnessType.RESPIRATORY: "مشکل تنفسی",
            IllnessType.WEAKNESS_FATIGUE: "ضعف و بی‌حالی",
            IllnessType.STROKE: "سکته مغزی",
            IllnessType.PSYCHIATRIC_DISORDER: "اختلال روانی",
            IllnessType.FEVER_SEIZURE: "تب و تشنج",
            IllnessType.HYPERTENSION: "افزایش فشار خون",
            IllnessType.HYPOGLYCEMIA: "هیپوگلیسمی (افت قند خون)",
            IllnessType.HYPERGLYCEMIA: "هایپرگلیسمی (افزایش قند خون)",
            IllnessType.DECREASED_CONSCIOUSNESS: "کاهش سطح هوشیاری",
            IllnessType.PHYSICAL_ASSAULT: "ضرب و جرح",
            IllnessType.HYSTERIA: "حمله هیستریک",
            IllnessType.ABDOMINAL_PAIN: "درد شکمی",
            IllnessType.RENAL_COLIC: "قولنج کلیوی",
            IllnessType.CHILDBIRTH: "زایمان",
            IllnessType.MISCARRIAGE: "سقط جنین",
        }[self]


class InjuryRole(Enum):
    """Role or position of the injured person in a vehicle accident."""

    DRIVER = "IsRanande"
    """The injured person was the driver of the vehicle."""
    PASSENGER = "IsSarneshin"
    """The injured person was a passenger in the vehicle."""
    PEDESTRIAN = "Aber"
    """The injured person was outside the vehicle, e.g., struck while walking."""
    UNKNOWN = "VaziatMasdoomIsNamoshakhas"
    """The injured person's role in the accident is unknown or unspecified."""

    @property
    def persian_label(self) -> str:
        """Persian label of the set injury role."""
        return {
            InjuryRole.DRIVER: "راننده",
            InjuryRole.PASSENGER: "سرنشین",
            InjuryRole.PEDESTRIAN: "عابر پیاده",
            InjuryRole.UNKNOWN: "نامشخص",
        }[self]


class VehicleType(Enum):
    """Type of vehicle or transport involved in a vehicle accident."""

    LIGHT_VEHICLE = "KhodroSabok"
    """A light motor vehicle such as a car or small van."""
    HEAVY_VEHICLE = "KhodroSangin"
    """A heavy vehicle such as a truck or bus."""
    MOTORCYCLE = "Motor"
    """A motorcycle involved in the accident."""
    BICYCLE = "Docharkhe"
    """A bicycle involved in the accident."""
    AIRCRAFT = "Havaei"
    """An aircraft involved in the accident."""
    WATERCRAFT = "Daryaei"
    """A watercraft or boat involved in the accident."""
    SURFACE_VEHICLE = "SathZamini"
    """A ground-level vehicle that doesn't fit standard categories (e.g., ATV)."""
    UNDERGROUND_VEHICLE = "ZirZamini"
    """A subway, tunnel vehicle, or other underground transport."""
    OTHER_TRANSPORT = "VasileNaghlieSayer"
    """Any other type of vehicle or transport not listed above."""

    @property
    def persian_label(self) -> str:
        """Persian label of the set vehicle type."""
        return {
            VehicleType.LIGHT_VEHICLE: "خودرو سبک",
            VehicleType.HEAVY_VEHICLE: "خودرو سنگین",
            VehicleType.MOTORCYCLE: "موتورسیکلت",
            VehicleType.BICYCLE: "دوچرخه",
            VehicleType.AIRCRAFT: "وسیله هوایی",
            VehicleType.WATERCRAFT: "وسیله دریایی",
            VehicleType.SURFACE_VEHICLE: "وسیله نقلیه سطح زمینی",
            VehicleType.UNDERGROUND_VEHICLE: "وسیله نقلیه زیرزمینی",
            VehicleType.OTHER_TRANSPORT: "سایر وسایل نقلیه",
        }[self]


@dataclass(slots=True)
class LocationAndEmergency:
    """Holds information about location and emergency type."""

    address: str | None
    """Address or emergency location"""
    chief_complaint: str | None
    """Primary reason for emergency call"""
    location_type: LocationType | None
    """Type of emergency location"""
    location_other_info: str | None
    """Other information about emergency location"""
    accident_type: AccidentType | None
    """Type of emergency accident"""
    illness_type: IllnessType | None
    """Type of emergency illness"""
    is_vehicle_accident: bool
    """Whether the emergency is vehicle related accident"""
    emergency_type_other_info: str | None
    """Other information about emergency type"""
    role_in_accident: InjuryRole | None
    """Role or position of the injured person in a vehicle accident"""
    role_in_accident_other_info: str | None
    """Other information about role in accident"""
    vehicle_type: VehicleType | None
    """Type of the vehicle the patient is related"""
