from __future__ import annotations
from enum import auto, StrEnum
from dataclasses import dataclass
from datetime import datetime


class ContractType(StrEnum):
    PROCURMENT = auto()
    TRANSPORT = auto()
    SHUTTLE = auto()


class WaypointType(StrEnum):
    NEUTRON_STAR = auto()
    RED_STAR = auto()
    ORANGE_STAR = auto()
    BLUE_STAR = auto()
    YOUNG_STAR = auto()
    WHITE_DWARF = auto()
    BLACK_HOLE = auto()
    HYPERGIANT = auto()
    NEBULA = auto()
    UNSTABLE = auto()


class Goods(StrEnum):
    PRECIOUS_STONES = auto()
    QUARTZ_SAND = auto()
    SILICON_CRYSTALS = auto()
    AMMONIA_ICE = auto()
    LIQUID_HYDROGEN = auto()
    LIQUID_NITROGEN = auto()
    ICE_WATER = auto()
    EXOTIC_MATTER = auto()
    ADVANCED_CIRCUITRY = auto()
    GRAVITON_EMITTERS = auto()
    IRON = auto()
    IRON_ORE = auto()
    COPPER = auto()
    COPPER_ORE = auto()
    ALUMINUM = auto()
    ALUMINUM_ORE = auto()
    SILVER = auto()
    SILVER_ORE = auto()
    GOLD = auto()
    GOLD_ORE = auto()
    PLATINUM = auto()
    PLATINUM_ORE = auto()
    DIAMONDS = auto()
    URANITE = auto()
    URANITE_ORE = auto()
    MERITIUM = auto()
    MERITIUM_ORE = auto()
    HYDROCARBON = auto()
    ANTIMATTER = auto()
    FERTILIZERS = auto()
    FABRICS = auto()
    FOOD = auto()
    JEWELRY = auto()
    MACHINERY = auto()
    FIREARMS = auto()
    ASSAULT_RIFLES = auto()
    MILITARY_EQUIPMENT = auto()
    EXPLOSIVES = auto()
    LAB_INSTRUMENTS = auto()
    AMMUNITION = auto()
    ELECTRONICS = auto()
    SHIP_PLATING = auto()
    EQUIPMENT = auto()
    FUEL = auto()
    MEDICINE = auto()
    DRUGS = auto()
    CLOTHING = auto()
    MICROPROCESSORS = auto()
    PLASTICS = auto()
    POLYNUCLEOTIDES = auto()
    BIOCOMPOSITES = auto()
    NANOBOTS = auto()
    AI_MAINFRAMES = auto()
    QUANTUM_DRIVES = auto()
    ROBOTIC_DRONES = auto()
    CYBER_IMPLANTS = auto()
    GENE_THERAPEUTICS = auto()
    NEURAL_CHIPS = auto()
    MOOD_REGULATORS = auto()
    VIRAL_AGENTS = auto()
    MICRO_FUSION_GENERATORS = auto()
    SUPERGRAINS = auto()
    LASER_RIFLES = auto()
    HOLOGRAPHICS = auto()
    SHIP_SALVAGE = auto()
    RELIC_TECH = auto()
    NOVEL_LIFEFORMS = auto()
    BOTANICAL_SPECIMENS = auto()
    CULTURAL_ARTIFACTS = auto()
    REACTOR_SOLAR_I = auto()
    REACTOR_FUSION_I = auto()
    REACTOR_FISSION_I = auto()
    REACTOR_CHEMICAL_I = auto()
    REACTOR_ANTIMATTER_I = auto()
    ENGINE_IMPULSE_DRIVE_I = auto()
    ENGINE_ION_DRIVE_I = auto()
    ENGINE_ION_DRIVE_II = auto()
    ENGINE_HYPER_DRIVE_I = auto()
    MODULE_MINERAL_PROCESSOR_I = auto()
    MODULE_CARGO_HOLD_I = auto()
    MODULE_CREW_QUARTERS_I = auto()
    MODULE_ENVOY_QUARTERS_I = auto()
    MODULE_PASSENGER_CABIN_I = auto()
    MODULE_MICRO_REFINERY_I = auto()
    MODULE_ORE_REFINERY_I = auto()
    MODULE_FUEL_REFINERY_I = auto()
    MODULE_SCIENCE_LAB_I = auto()
    MODULE_JUMP_DRIVE_I = auto()
    MODULE_JUMP_DRIVE_II = auto()
    MODULE_JUMP_DRIVE_III = auto()
    MODULE_WARP_DRIVE_I = auto()
    MODULE_WARP_DRIVE_II = auto()
    MODULE_WARP_DRIVE_III = auto()
    MODULE_SHIELD_GENERATOR_I = auto()
    MODULE_SHIELD_GENERATOR_II = auto()
    MOUNT_GAS_SIPHON_I = auto()
    MOUNT_GAS_SIPHON_II = auto()
    MOUNT_GAS_SIPHON_III = auto()
    MOUNT_SURVEYOR_I = auto()
    MOUNT_SURVEYOR_II = auto()
    MOUNT_SURVEYOR_III = auto()
    MOUNT_SENSOR_ARRAY_I = auto()
    MOUNT_SENSOR_ARRAY_II = auto()
    MOUNT_SENSOR_ARRAY_III = auto()
    MOUNT_MINING_LASER_I = auto()
    MOUNT_MINING_LASER_II = auto()
    MOUNT_MINING_LASER_III = auto()
    MOUNT_LASER_CANNON_I = auto()
    MOUNT_MISSILE_LAUNCHER_I = auto()
    MOUNT_TURRET_I = auto()


class FactionSymbols(StrEnum):
    COSMIC = auto()
    VOID = auto()
    GALACTIC = auto()
    QUANTUM = auto()
    DOMINION = auto()
    ASTRO = auto()
    CORSAIRS = auto()
    OBSIDIAN = auto()
    AEGIS = auto()
    


@dataclass
class Agent:
    accountId: str
    symbol: str
    headquarters: str
    credits: int
    startingFaction: str



@dataclass
class Chart:
    waypointSymbol: str
    submittedBy: str
    submittedOn: datetime


@dataclass
class ConnectedSystem:
    symbol: str
    sectorSymbol: str
    type_: WaypointType
    factionSymbol: str
    x: int
    y: int
    distance: int



@dataclass
class Contract:
    id_: str
    factionSymbol: str
    type_: ContractType
    terms: ContractTerms
    accepted: bool
    fulfilled: bool
    expiration: datetime | None
    deadlineToAccept: datetime | None


@dataclass
class ContractDeliverGood:
    tradeSymbol: str
    destinationSymbol: str
    unitsRequired: int
    unitsFulfilled: int


@dataclass
class ContractPayment:
    onAccepted: int
    onFulfilled: int


@dataclass
class ContractTerms:
    deadline: datetime
    payment: ContractPayment
    deliver: list[ContractDeliverGood]


@dataclass
class Cooldown:
    shipSymbol: str
    totalSeconds: int
    remainingSeconds: int
    expiration: datetime


@dataclass
class Extraction:
    shipSymbol: str
    yield_: ExtractionYield


@dataclass
class ExtractionYield:
    symbol: Goods
    units: int


@dataclass
class Faction:
    symbol: FactionSymbols
    name: str
    description: str
    headquarters: str
    traits: list[FactionTrait]
    isRecruiting: bool


