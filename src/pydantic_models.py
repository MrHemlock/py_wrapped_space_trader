from __future__ import annotations

from enum import auto, StrEnum
from datetime import datetime
from typing import Any, Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)
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


class ApiModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)


class ContractType(SymbolEnums):
    PROCURMENT = auto()
    TRANSPORT = auto()
    SHUTTLE = auto()


class DepositType(SymbolEnums):
    QUARTZ_SAND = auto()
    SILICON_CRYSTALS = auto()
    PRECIOUS_STONES = auto()
    ICE_WATER = auto()
    AMMONIA_ICE = auto()
    IRON_ORE = auto()
    COPPER_ORE = auto()
    SILVER_ORE = auto()
    ALUMINUM_ORE = auto()
    GOLD_ORE = auto()
    PLATINUM_ORE = auto()
    DIAMONDS = auto()
    URANITE_ORE = auto()
    MERITIUM_ORE = auto()


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
    UNITED = auto()
    SOLITARY = auto()
    OMEGA = auto()
    ECHO = auto()
    LORDS = auto()
    CULT = auto()
    ANCIENTS = auto()
    SHADOW = auto()
    ETHERAL = auto()


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


class ShipEngineType(SymbolEnums):
    ENGINE_IMPULSE_DRIVE_I = auto()
    ENGINE_ION_DRIVE_I = auto()
    ENGINE_ION_DRIVE_II = auto()
    ENGINE_HYPER_DRIVE_I = auto()


class ShipFrameType(SymbolEnums):
    FRAME_PROBE = auto()
    FRAME_DRONE = auto()
    FRAME_INTERCEPTOR = auto()
    FRAME_RACER = auto()
    FRAME_FIGHTER = auto()
    FRAME_FRIGATE = auto()
    FRAME_SHUTTLE = auto()
    FRAME_EXPLORER = auto()
    FRAME_MINER = auto()
    FRAME_LIGHT_FREIGHTER = auto()
    FRAME_HEAVY_FREIGHTER = auto()
    FRAME_TRANSPORT = auto()
    FRAME_DESTROYER = auto()
    FRAME_CRUISER = auto()
    FRAME_CARRIER = auto()


class ShipModuleType(SymbolEnums):
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


class ShipMountType(SymbolEnums):
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


class ShipNavFlightMode(SymbolEnums):
    DRIFT = auto()
    STEALTH = auto()
    CRUISE = auto()
    BURN = auto()


class ShipNavStatus(SymbolEnums):
    IN_TRANSIT = auto()
    IN_ORBIT = auto()
    DOCKED = auto()


class ShipReactorType(SymbolEnums):
    REACTOR_SOLAR_I = auto()
    REACTOR_FUSION_I = auto()
    REACTOR_FISSION_I = auto()
    REACTOR_CHEMICAL_I = auto()
    REACTOR_ANTIMATTER_I = auto()


class ShipRole(SymbolEnums):
    FABRICATOR = auto()
    HARVESTER = auto()
    HAULER = auto()
    INTERCEPTOR = auto()
    EXCAVATOR = auto()
    TRANSPORT = auto()
    REPAIR = auto()
    SURVEYOR = auto()
    COMMAND = auto()
    CARRIER = auto()
    PATROL = auto()
    SATELLITE = auto()
    EXPLORER = auto()
    REFINERY = auto()


class SystemType(SymbolEnums):
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


class TransactionType(SymbolEnums):
    PURCHASE = auto()
    SELL = auto()


class WaypointType(SymbolEnums):
    PLANET = auto()
    GAS_GIANT = auto()
    MOON = auto()
    ORBITAL_STATION = auto()
    JUMP_GATE = auto()
    ASTEROID_FIELD = auto()
    NEBULA = auto()
    DEBRIS_FIELD = auto()
    GRAVITY_WELL = auto()


class WaypointTypeSymbol(SymbolEnums):
    UNCHARTED = auto()
    MARKETPLACE = auto()
    SHIPYARD = auto()
    OUTPOST = auto()
    SCATTERED_SETTLEMENTS = auto()
    SPRAWLING_CITIES = auto()
    MEGA_STRUCTURES = auto()
    OVERCROWDED = auto()
    HIGH_TECH = auto()
    CORRUPT = auto()
    BUREAUCRATIC = auto()
    TRADING_HUB = auto()
    INDUSTRIAL = auto()
    BLACK_MARKET = auto()
    RESEARCH_FACILITY = auto()
    MILITARY_BASE = auto()
    SURVEILLANCE_OUTPOST = auto()
    EXPLORATION_OUTPOST = auto()
    MINERAL_DEPOSITS = auto()
    COMMON_METAL_DEPOSITS = auto()
    PRECIOUS_METAL_DEPOSITS = auto()
    RARE_METAL_DEPOSITS = auto()
    METHANE_POOLS = auto()
    ICE_CRYSTALS = auto()
    EXPLOSIVE_GASES = auto()
    STRONG_MAGNETOSPHERE = auto()
    VIBRANT_AURORAS = auto()
    SALT_FLATS = auto()
    CANYONS = auto()
    PERPETUAL_DAYLIGHT = auto()
    PERPETUAL_OVERCAST = auto()
    DRY_SEABEDS = auto()
    MAGMA_SEAS = auto()
    SUPERVOLCANOES = auto()
    ASH_CLOUDS = auto()
    VAST_RUINS = auto()
    MUTATED_FLORA = auto()
    TERRAFORMED = auto()
    EXTREME_TEMPERATURES = auto()
    EXTREME_PRESSURE = auto()
    DIVERSE_LIFE = auto()
    SCARCE_LIFE = auto()
    FOSSILS = auto()
    WEAK_GRAVITY = auto()
    STRONG_GRAVITY = auto()
    CRUSHING_GRAVITY = auto()
    TOXIC_ATMOSPHERE = auto()
    CORROSIVE_ATMOSPHERE = auto()
    BREATHABLE_ATMOSPHERE = auto()
    JOVIAN = auto()
    ROCKY = auto()
    VOLCANIC = auto()
    FROZEN = auto()
    SWAMP = auto()
    BARREN = auto()
    TEMPERATE = auto()
    JUNGLE = auto()
    OCEAN = auto()
    STRIPPED = auto()


class Agent(ApiModel):
    account_id: str = Field(min_length=1) 
    symbol: str = Field(min_length=3, max_length=14)
    headquarters: str
    credits: int
    starting_faction: str = Field(min_length=1)
    ship_count: int


class Chart(ApiModel):
    waypoint_symbol: str
    submitted_by: str
    submitted_on: datetime


class ConnectedSystem(ApiModel):
    symbol: str = Field(min_length=1)
    sector_symbol: str = Field(min_length=1)
    type: SystemType
    faction_symbol: FactionSymbols
    x: int
    y: int
    distance: int


class Contract(ApiModel):
    id: str = Field(min_length=1)
    faction_symbol: FactionSymbols
    type: ContractType
    terms: ContractTerms
    accepted: bool = False
    fulfilled: bool = False
    expiration: datetime | None
    deadline_to_accept: datetime | None


class ContractDeliverGood(ApiModel):
    trade_symbol: TradeGoodsSymbols
    destination_symbol: str = Field(min_length=1)
    units_required: int
    units_fulfilled: int


class ContractPayment(ApiModel):
    on_accepted: int
    on_fulfilled: int


class ContractTerms(ApiModel):
    deadline: datetime
    payment: ContractPayment
    deliver: list[ContractDeliverGood]


class Cooldown(ApiModel):
    ship_symbol: str = Field(min_length=1)
    total_seconds: int = Field(ge=0)
    remaining_seconds: int = Field(ge=0)
    expiration: datetime


class Extraction(ApiModel):
    ship_symbol: str = Field(min_length=1)
    yield_: ExtractionYield


class ExtractionYield(ApiModel):
    symbol: TradeGoodsSymbols
    units: int


class Faction(ApiModel):
    symbol: FactionSymbols
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    headquarters: str = Field(min_length=1)
    traits: list[FactionTrait]
    is_recruiting: bool


class FactionTrait(ApiModel):
    symbol: FactionTraitSymbols
    name: str
    description: str


class JumpGate(ApiModel):
    jump_range: int
    faction_symbol: FactionSymbols
    connected_systems: list[System]


class Market(ApiModel):
    symbol: str
    exports: list[TradeGood]
    imports: list[TradeGood]
    exchange: list[TradeGood]
    transactions: list[MarketTransaction]
    trade_goods: list[MarketTradeGood]


class MarketTradeGood(ApiModel):
    symbol: TradeGoodsSymbols
    trade_volume: int = Field(ge=1)
    supply: MarketSupply
    purchase_price: int = Field(ge=0)
    sell_price: int = Field(ge=0)


class MarketTransaction(ApiModel):
    waypoint_symbol: str
    ship_symbol: str
    trade_symbol: TradeGoodsSymbols
    type_: Literal["PURCHASE"] | Literal["SELL"]
    units: int = Field(ge=0)
    price_per_unit: int = Field(ge=0)
    total_price: int = Field(ge=0)
    timestamp: datetime


class Meta(ApiModel):
    total: int = Field(ge=0)
    page: int = Field(ge=1, default=1)  # type: ignore
    limit: int = Field(ge=1, le=20, default=10) # type: ignore


class ScannedShip(ApiModel):
    symbol: str
    registration: ShipRegistration
    nav: ShipNav
    frame: dict[str, ShipFrameType]
    reactor: dict[str, ShipReactorType]
    engine: dict[str, ShipEngineType]
    mounts: dict[str, ShipMountType]
    

class ScannedSystem(ApiModel):
    symbol: str = Field(min_length=1)
    sector_symbol: str = Field(min_length=1)
    type: SystemType
    x: int
    y: int
    distance: int


class ScannedWaypoint(ApiModel):
    symbol: str = Field(min_length=1)
    type: WaypointType
    system_symbol: str = Field(min_length=1)
    x: int
    y: int
    orbitals: list[Waypoint]
    faction: FactionSymbols
    traits: list[WaypointTrait]
    chart: Chart


class Ship(ApiModel):
    symbol: str
    registration: ShipRegistration
    nav: ShipNav
    crew: ShipCrew
    frame: ShipFrame
    reactor: ShipReactor
    engine: ShipEngine
    cooldown: Cooldown
    modules: list[ShipModule]
    mounts: list[ShipMount]
    cargo: ShipCargo
    fuel: ShipFuel


class ShipCargo(ApiModel):
    capacity: int = Field(ge=0)
    units: int = Field(ge=0)
    inventory: list[ShipCargoItem]


class ShipCargoItem(ApiModel):
    symbol: str
    name: str
    description: str
    units: int = Field(ge=1)


class ShipCondition(ApiModel):
    value: int = Field(ge=0, le=100) # type: ignore


class ShipCrew(ApiModel):
    current: int
    required: int
    capacity: int
    rotation: Literal["STRICT"] | Literal["RELAXED"] = "STRICT"
    morale: int = Field(ge=0, le=100)
    wages: int = Field(ge=0)


class ShipEngine(ApiModel):
    symbol: ShipEngineType
    name: str
    description: str
    condition: ShipCondition
    speed: int = Field(ge=1)
    requirements: ShipRequirements


class ShipFrame(ApiModel):
    symbol: ShipFrameType
    name: str
    description: str
    condition: ShipCondition
    module_slots: int = Field(ge=0)
    mounting_points: int = Field(ge=0)
    fuel_capacity: int = Field(ge=0)
    requirements: ShipRequirements


class ShipFuel(ApiModel):
    current: str = Field(ge=0)
    capacity: int = Field(ge=0)
    consumed: ShipFuelConsumed


class ShipFuelConsumed(ApiModel):
    amount: int = Field(ge=0)
    timestamp: datetime


class ShipModificationTransaction(ApiModel):
    waypoint_symbol: str
    ship_symbol: str
    trade_symbol: TradeGoodsSymbols
    total_price: int = Field(ge=0)
    timestamp: datetime


class ShipModule(ApiModel):
    symbol: ShipModuleType
    capacity: int = Field(ge=0)
    range: int = Field(ge=0)
    name: str
    description: str
    requirements: ShipRequirements


class ShipMount(ApiModel):
    symbol: ShipMountType
    name: str
    description: str
    strength: int = Field(ge=0)
    deposits: list[DepositType]
    requirements: ShipRequirements


class ShipNav(ApiModel):
    system_symbol: str
    waypoint_symbol: str
    route: ShipNavRoute
    status: ShipNavStatus
    flight_mode: ShipNavFlightMode = ShipNavFlightMode.CRUISE


class ShipNavRoute(ApiModel):
    destination: ShipNavRouteWaypoint
    origin: ShipNavRouteWaypoint
    departure_time: datetime
    arrival: datetime


class ShipNavRouteWaypoint(ApiModel):
    symbol: str = Field(min_length=1)
    type: WaypointType
    system_symbol: str = Field(min_length=1)
    x: int
    y: int


class ShipReactor(ApiModel):
    symbol: ShipReactorType
    name: str
    description: str
    condition: int = Field(ge=0, le=100) # type: ignore
    power_outage: int = Field(ge=1) # type: ignore
    requirements: ShipRequirements


class ShipRegistration(ApiModel):
    name: str = Field(min_length=1)
    faction_symbol: str = Field(min_length=1)
    role: ShipRole


class ShipRequirements(ApiModel):
    power: int
    crew: int
    slots: int


class Shipyard(ApiModel):
    symbol: str = Field(ge=1)
    ship_types: list[dict[str, ShipType]]
    transactions: list[ShipyardTransaction]
    ships: list[Ship]
    modifications_fee: int


class ShipyardShip(ApiModel):
    type: ShipType
    name: str
    purchase_price: int
    frame: ShipFrame
    reactor: ShipReactor
    engine: ShipEngine
    modules: list[ShipModule]
    mounts: list[ShipMount]
    crew: ShipCrew


class ShipyardTransaction(ApiModel):
    waypoint_symbol: str
    ship_symbol: str
    price: int = Field(ge=0)
    agent_symbol: str
    timestampe: datetime


class Survey(ApiModel):
    signature: str = Field(min_length=1)
    symbol: str = Field(min_length=1)
    deposits: list[SurveyDeposit]
    expiration: datetime
    size: Literal["SMALL"] | Literal["MODERATE"] | Literal["LARGE"]


class System(ApiModel):
    symbol: str = Field(min_length=1)
    sector_symbol: str = Field(min_length=1)
    type: SystemType
    x: int
    y: int
    waypoints: list[SystemWaypoint]
    factions: list[FactionSymbols]


class SystemWaypoint(ApiModel):
    symbol: str
    type: SystemType
    x: int
    y: int
    orbitals: list[WaypointOrbital]
    orbits: WaypointOrbital


class WaypointOrbital(ApiModel):
    symbol: str = Field(min_length=1)


class Waypoint(ApiModel):
    symbol: str = Field(min_length=1)
    type: SystemType
    system_symbol: str = Field(min_length=1)
    x: int
    y: int
    orbitals: list[WaypointOrbital]
    orbits: str = Field(min_length=1)
    faction: FactionSymbols
    traits: list[FactionTrait]
    chart: Chart


class WaypointTrait(ApiModel):
    symbol: WaypointTypeSymbol
    name: str
    description: str


class SurveyDeposit(ApiModel):
    symbol: str


class TradeGood:
    symbol: TradeGoodsSymbols
    name: str
    description: str
