from __future__ import annotations

from enum import auto, StrEnum
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, ValidationError
from pydantic.alias_generators import to_camel


class SymbolEnums(StrEnum):
    @staticmethod
    def _generate_next_value_(
        name: str,
        start: int,
        count: int,
        last_values: list[Any],
    ) -> Any:
        return name.upper()


class ApiNamingModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)


class ContractType(SymbolEnums):
    PROCURMENT = auto()
    TRANSPORT = auto()
    SHUTTLE = auto()


class WaypointType(SymbolEnums):
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


class TradeGoodsSymbols(SymbolEnums):
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


class FactionSymbols(SymbolEnums):
    COSMIC = auto()
    VOID = auto()
    GALACTIC = auto()
    QUANTUM = auto()
    DOMINION = auto()
    ASTRO = auto()
    CORSAIRS = auto()
    OBSIDIAN = auto()
    AEGIS = auto()


class FactionTraitSymbols(SymbolEnums):
    BUREAUCRATIC = auto()
    SECRETIVE = auto()
    CAPITALISTIC = auto()
    INDUSTRIOUS = auto()
    PEACEFUL = auto()
    DISTRUSTFUL = auto()
    WELCOMING = auto()
    SMUGGLERS = auto()
    SCAVENGERS = auto()
    REBELLIOUS = auto()
    EXILES = auto()
    PIRATES = auto()
    RAIDERS = auto()
    CLAN = auto()
    GUILD = auto()
    DOMINION = auto()
    FRINGE = auto()
    FORSAKEN = auto()
    ISOLATED = auto()
    LOCALIZED = auto()
    ESTABLISHED = auto()
    NOTABLE = auto()
    DOMINANT = auto()
    INESCAPABLE = auto()
    INNOVATIVE = auto()
    BOLD = auto()
    VISIONARY = auto()
    CURIOUS = auto()
    DARING = auto()
    EXPLORATORY = auto()
    RESOURCEFUL = auto()
    FLEXIBLE = auto()
    COOPERATIVE = auto()
    UNITED = auto()
    STRATEGIC = auto()
    INTELLIGENT = auto()
    RESEARCH_FOCUSED = auto()
    COLLABORATIVE = auto()
    PROGRESSIVE = auto()
    MILITARISTIC = auto()
    TECHNOLOGICALLY_ADVANCED = auto()
    AGGRESSIVE = auto()
    IMPERIALISTIC = auto()
    TREASURE_HUNTERS = auto()
    DEXTEROUS = auto()
    UNPREDICTABLE = auto()
    BRUTAL = auto()
    FLEETING = auto()
    ADAPTABLE = auto()
    SELF_SUFFICIENT = auto()
    DEFENSIVE = auto()
    PROUD = auto()
    DIVERSE = auto()
    INDEPENDENT = auto()
    SELF_INTERESTED = auto()
    FRAGMENTED = auto()
    COMMERCIAL = auto()
    FREE_MARKETS = auto()
    ENTREPRENEURIAL = auto()


class MarketSupply(SymbolEnums):
    SCARCE = auto()
    LIMITED = auto()
    MODERATE = auto()
    ABUNDANT = auto()


class TransactionType(SymbolEnums):
    PURCHASE = auto()
    SELL = auto()


class ShipType(SymbolEnums):
    SHIP_PROBE = auto()
    SHIP_MINING_DRONE = auto()
    SHIP_INTERCEPTOR = auto()
    SHIP_LIGHT_HAULER = auto()
    SHIP_COMMAND_FRIGATE = auto()
    SHIP_EXPLORER = auto()
    SHIP_HEAVY_FREIGHTER = auto()
    SHIP_LIGHT_SHUTTLE = auto()
    SHIP_ORE_HOUND = auto()
    SHIP_REFINING_FREIGHTER = auto()


class Agent(ApiNamingModel):
    account_id: str
    symbol: str
    headquarters: str
    credits: int
    starting_faction: str


class Chart(ApiNamingModel):
    waypoint_symbol: str
    submitted_by: str
    submitted_on: datetime


class ConnectedSystem(ApiNamingModel):
    symbol: str
    sector_symbol: str
    type: WaypointType
    faction_symbol: FactionSymbols
    x: int
    y: int
    distance: int


class Contract(ApiNamingModel):
    id: str
    faction_symbol: FactionSymbols
    type: ContractType
    terms: ContractTerms
    accepted: bool
    fulfilled: bool
    expiration: datetime | None
    deadline_to_accept: datetime | None


class ContractDeliverGood(ApiNamingModel):
    trade_symbol: TradeGoodsSymbols
    destination_symbol: str
    units_required: int
    units_fulfilled: int


class ContractPayment(ApiNamingModel):
    on_accepted: int
    on_fulfilled: int


class ContractTerms(ApiNamingModel):
    deadline: datetime
    payment: ContractPayment
    deliver: list[ContractDeliverGood]


class Cooldown(ApiNamingModel):
    ship_symbol: str
    total_seconds: int
    remaining_seconds: int
    expiration: datetime


class Extraction(ApiNamingModel):
    ship_symbol: str
    yield_: ExtractionYield


class ExtractionYield(ApiNamingModel):
    symbol: TradeGoodsSymbols
    units: int


class Faction(ApiNamingModel):
    symbol: FactionSymbols
    name: str
    description: str
    headquarters: str
    traits: list[FactionTrait]
    is_recruiting: bool


class FactionTrait(ApiNamingModel):
    symbol: FactionTraitSymbols
    name: str
    description: str
